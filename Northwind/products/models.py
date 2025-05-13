from django.db import models

class Product(models.Model):
    ProductID = models.AutoField(primary_key=True, db_column='ProductID')
    ProductName = models.CharField(max_length=40, db_column='ProductName')
    SupplierID = models.IntegerField(blank=True, null=True, db_column='SupplierID')
    CategoryID = models.IntegerField(blank=True, null=True, db_column='CategoryID')
    QuantityPerUnit = models.CharField(max_length=20, blank=True, null=True, db_column='QuantityPerUnit')
    UnitPrice = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, db_column='UnitPrice')
    UnitsInStock = models.SmallIntegerField(blank=True, null=True, db_column='UnitsInStock')
    UnitsOnOrder = models.SmallIntegerField(blank=True, null=True, db_column='UnitsOnOrder')
    ReorderLevel = models.SmallIntegerField(blank=True, null=True, db_column='ReorderLevel')
    Discontinued = models.BooleanField(db_column='Discontinued')

    class Meta:
        db_table = 'Products'
        managed = False

    def __str__(self):
        return self.ProductName