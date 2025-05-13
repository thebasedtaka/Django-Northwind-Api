from django.db import models

class Category(models.Model):
    CategoryID = models.AutoField(primary_key=True, db_column='CategoryID')
    CategoryName = models.CharField(max_length=15, db_column='CategoryName')
    Description = models.TextField(blank=True, null=True, db_column='Description')
    Picture = models.BinaryField(blank=True, null=True, db_column='Picture')

    class Meta:
        db_table = 'Categories'
        managed = False
        
    def __str__(self):
        return self.CategoryName