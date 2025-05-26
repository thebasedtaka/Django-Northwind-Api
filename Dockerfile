FROM python:3.11-slim-bookworm

# Set working directory to project root (where manage.py lives)
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    unixodbc-dev gcc python3-dev curl gnupg && \
    rm -rf /var/lib/apt/lists/*

# Install SQL Server ODBC Driver
RUN curl -fsSL https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > /etc/apt/keyrings/packages.microsoft.gpg && \
    echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/packages.microsoft.gpg] https://packages.microsoft.com/debian/12/prod bookworm main" > /etc/apt/sources.list.d/mssql-release.list && \
    apt-get update && \
    ACCEPT_EULA=Y apt-get install -y msodbcsql17 && \
    rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy entire project
COPY . .

# Set environment variables
ENV PYTHONPATH=/app/Northwind
ENV DJANGO_SETTINGS_MODULE=Northwind.Northwind.settings
ENV PORT=8000

RUN python manage.py collectstatic --noinput

# Run Gunicorn (correct module path)
CMD ["/bin/sh", "-c", "gunicorn Northwind.Northwind.wsgi:application --bind 0.0.0.0:${PORT} --workers 2 --timeout 120"]