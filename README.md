# Northwind Database Django REST API

A Django REST API for the classic Northwind database, providing a comprehensive backend service for managing products, orders, customers, and more.

## Project Overview

This project is a Django-based REST API that connects to the Northwind database hosted on Azure SQL. It provides endpoints for accessing and manipulating data from various entities in the Northwind database, including:

- Categories
- Customers
- Employees
- Orders and Order Details
- Products
- Regions and Territories
- Shippers
- Suppliers

## Technologies Used

- Python 3.x
- Django 5.0.x
- Django REST Framework
- Microsoft SQL Server (Azure SQL)
- ODBC Driver for SQL Server

## Setup and Installation

### Prerequisites

- Python 3.x
- Virtual Environment
- ODBC Driver 17 for SQL Server
- Azure SQL Database access

### Installation Steps

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/northwind-django-api.git
   cd northwind-django-api
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the Northwind directory with the following variables:
   ```
   AZURESQL_USER=your_username
   AZURESQL_PASSWORD=your_password
   AZURESQL_HOSTNAME=your_azure_sql_server.database.windows.net
   AZURESQL_PORT=1433
   AZURESQL_DATABASE=Northwind
   ```

5. Run migrations (if needed):
   ```
   python manage.py migrate
   ```

6. Start the development server:
   ```
   python manage.py runserver
   ```

## API Endpoints

The API provides the following endpoints:

- `/api/categories/` - Categories management
- `/api/customers/` - Customers management
- `/api/employees/` - Employees management
- `/api/territories/` - Territories management
- `/api/employeeterritories/` - Employee territories management
- `/api/orders/` - Orders management
- `/api/orderdetails/` - Order details management
- `/api/products/` - Products management
- `/api/regions/` - Regions management
- `/api/shippers/` - Shippers management
- `/api/suppliers/` - Suppliers management

## Project Structure

```
Northwind/
├── categories/         # Categories app
├── customers/          # Customers app
├── employees/          # Employees app
├── Northwind/          # Main project settings
├── orders/             # Orders app
├── products/           # Products app
├── regions/            # Regions app
├── shippers/           # Shippers app
├── suppliers/          # Suppliers app
├── .env                # Environment variables
├── db.sqlite3          # Local SQLite database (if used)
└── manage.py           # Django management script
```

## Development

### Adding New Features

1. Create a new app if needed:
   ```
   python manage.py startapp new_app_name
   ```

2. Add models, serializers, and views
3. Register the app in `INSTALLED_APPS` in settings.py
4. Add URL patterns in urls.py

## Security Notes

- The project uses environment variables for sensitive information
- Make sure to keep your `.env` file secure and never commit it to version control
- For production, ensure DEBUG is set to False and update ALLOWED_HOSTS

## Frontend Integration

The API is configured with CORS support for frontend applications running on:
- http://localhost:5173
- http://127.0.0.1:5173

## License

[Your License Here]

## Contributors

- [Your Name]

## Acknowledgements

- This project uses the Northwind database, a sample database originally created by Microsoft for Microsoft Access.