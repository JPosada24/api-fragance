from django.db import models
from categories.models import Category

# Create your models here.

class Product(models.Model):
  name = models.CharField(max_length=50)
  description = models.CharField(max_length=255)
  price = models.DecimalField(max_digits=10, decimal_places=2)
  stock = models.IntegerField()
  image = models.ImageField(upload_to='images/')
  category = models.ForeignKey(Category, on_delete=models.CASCADE)