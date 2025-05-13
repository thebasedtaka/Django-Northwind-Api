from django.db import models

class Order(models.Model):
    OrderID = models.AutoField(primary_key=True, db_column='OrderID')
    CustomerID = models.CharField(max_length=5, blank=True, null=True, db_column='CustomerID')
    EmployeeID = models.IntegerField(blank=True, null=True, db_column='EmployeeID')
    OrderDate = models.DateTimeField(blank=True, null=True, db_column='OrderDate')
    RequiredDate = models.DateTimeField(blank=True, null=True, db_column='RequiredDate')
    ShippedDate = models.DateTimeField(blank=True, null=True, db_column='ShippedDate')
    ShipVia = models.IntegerField(blank=True, null=True, db_column='ShipVia')
    Freight = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, db_column='Freight')
    ShipName = models.CharField(max_length=40, blank=True, null=True, db_column='ShipName')
    ShipAddress = models.CharField(max_length=60, blank=True, null=True, db_column='ShipAddress')
    ShipCity = models.CharField(max_length=15, blank=True, null=True, db_column='ShipCity')
    ShipRegion = models.CharField(max_length=15, blank=True, null=True, db_column='ShipRegion')
    ShipPostalCode = models.CharField(max_length=10, blank=True, null=True, db_column='ShipPostalCode')
    ShipCountry = models.CharField(max_length=15, blank=True, null=True, db_column='ShipCountry')

    class Meta:
        db_table = 'Orders'
        managed = False

    def __str__(self):
        return f"Order #{self.OrderID}"

class OrderDetail(models.Model):
    OrderID = models.IntegerField(primary_key=True, db_column='OrderID')
    ProductID = models.IntegerField(db_column='ProductID')
    UnitPrice = models.DecimalField(max_digits=19, decimal_places=4, db_column='UnitPrice')
    Quantity = models.SmallIntegerField(db_column='Quantity')
    Discount = models.FloatField(db_column='Discount')

    class Meta:
        db_table = 'Order Details'
        managed = False
        unique_together = (('OrderID', 'ProductID'),)

    def __str__(self):
        return f"Order {self.OrderID} - Product {self.ProductID} (Qty: {self.Quantity})"