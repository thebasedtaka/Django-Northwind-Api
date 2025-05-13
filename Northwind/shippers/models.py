from django.db import models

class Shipper(models.Model):
    ShipperID = models.AutoField(primary_key=True, db_column='ShipperID')
    CompanyName = models.CharField(max_length=40, db_column='CompanyName')
    Phone = models.CharField(max_length=24, blank=True, null=True, db_column='Phone')

    class Meta:
        db_table = 'Shippers'
        managed = False
        
    def __str__(self):
        return self.CompanyName