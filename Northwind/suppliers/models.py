from django.db import models

class Supplier(models.Model):
    SupplierID = models.AutoField(primary_key=True, db_column='SupplierID')
    CompanyName = models.CharField(max_length=40, db_column='CompanyName')
    ContactName = models.CharField(max_length=30, blank=True, null=True, db_column='ContactName')
    ContactTitle = models.CharField(max_length=30, blank=True, null=True, db_column='ContactTitle')
    Address = models.CharField(max_length=60, blank=True, null=True, db_column='Address')
    City = models.CharField(max_length=15, blank=True, null=True, db_column='City')
    Region = models.CharField(max_length=15, blank=True, null=True, db_column='Region')
    PostalCode = models.CharField(max_length=10, blank=True, null=True, db_column='PostalCode')
    Country = models.CharField(max_length=15, blank=True, null=True, db_column='Country')
    Phone = models.CharField(max_length=24, blank=True, null=True, db_column='Phone')
    Fax = models.CharField(max_length=24, blank=True, null=True, db_column='Fax')
    HomePage = models.TextField(blank=True, null=True, db_column='HomePage')

    class Meta:
        db_table = 'Suppliers'
        managed = False

        
    def __str__(self):
        return self.CompanyName