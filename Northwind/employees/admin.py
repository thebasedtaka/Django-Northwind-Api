from django.contrib import admin
from .models import Employee, Territory, EmployeeTerritory
# Register your models here.

admin.site.register(Employee)
admin.site.register(Territory)
admin.site.register(EmployeeTerritory)