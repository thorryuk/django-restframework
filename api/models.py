from pyexpat import model
from statistics import mode
from django.db import models

class Divisi(models.Model):
    
    reseller_id = models.IntegerField(null=True, blank=True)
    id_divisi = models.CharField(null=False, blank=False, max_length=50)
    nama_divisi = models.CharField(null=False, blank=False, max_length=75)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    
    class Meta:
        db_table = 'divisi'