from django.db import models

class Region(models.Model):
    RegionID = models.IntegerField(primary_key=True, db_column='RegionID')
    RegionDescription = models.CharField(max_length=50, db_column='RegionDescription')

    class Meta:
        db_table = 'Region'
        managed = False


    def __str__(self):
        return self.RegionDescription