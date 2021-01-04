from django.db import models

# Create your models here.
#DB定義

class Stock(models.Model):
        class Meta:
            db_table = 'stock'
        ticker = models.CharField(max_length=20)
        price = models.IntegerField()
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)