from django.db import models

class Employee(models.Model):
    EmployeeID = models.AutoField(primary_key=True, db_column='EmployeeID')
    LastName = models.CharField(max_length=20, db_column='LastName')
    FirstName = models.CharField(max_length=10, db_column='FirstName')
    Title = models.CharField(max_length=30, blank=True, null=True, db_column='Title')
    TitleOfCourtesy = models.CharField(max_length=25, blank=True, null=True, db_column='TitleOfCourtesy')
    BirthDate = models.DateTimeField(blank=True, null=True, db_column='BirthDate')
    HireDate = models.DateTimeField(blank=True, null=True, db_column='HireDate')
    Address = models.CharField(max_length=60, blank=True, null=True, db_column='Address')
    City = models.CharField(max_length=15, blank=True, null=True, db_column='City')
    Region = models.CharField(max_length=15, blank=True, null=True, db_column='Region')
    PostalCode = models.CharField(max_length=10, blank=True, null=True, db_column='PostalCode')
    Country = models.CharField(max_length=15, blank=True, null=True, db_column='Country')
    HomePhone = models.CharField(max_length=24, blank=True, null=True, db_column='HomePhone')
    Extension = models.CharField(max_length=4, blank=True, null=True, db_column='Extension')
    Photo = models.BinaryField(blank=True, null=True, db_column='Photo')
    Notes = models.TextField(blank=True, null=True, db_column='Notes')
    ReportsTo = models.IntegerField(blank=True, null=True, db_column='ReportsTo')
    PhotoPath = models.CharField(max_length=255, blank=True, null=True, db_column='PhotoPath')

    class Meta:
        db_table = 'Employees'
        managed = False


    def __str__(self):
        return f"{self.FirstName} {self.LastName}"

class Territory(models.Model):
    TerritoryID = models.CharField(primary_key=True, max_length=20, db_column='TerritoryID')
    TerritoryDescription = models.CharField(max_length=50, db_column='TerritoryDescription')
    RegionID = models.IntegerField(db_column='RegionID')

    class Meta:
        db_table = 'Territories'
        managed = False

    def __str__(self):
        return self.TerritoryDescription    

class EmployeeTerritory(models.Model):
    # Use one of the composite key fields as the primary key for Django
    EmployeeID = models.IntegerField(primary_key=True, db_column='EmployeeID')
    TerritoryID = models.CharField(max_length=20, db_column='TerritoryID')
    
    class Meta:
        db_table = 'EmployeeTerritories'
        managed = False
        # We still define unique_together for validation purposes
        unique_together = (('EmployeeID', 'TerritoryID'),)
    
    def __str__(self):
        return f"Employee {self.EmployeeID} - Territory {self.TerritoryID}"