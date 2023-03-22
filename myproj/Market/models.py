from django.db import models

# Create your models here.
class Display(models.Model):
    name= models.CharField(max_length=100)
    price= models.IntegerField()
    quantity = models.CharField(max_length=100)

# class Cart(models.Model):
#     cart= models.ForeignKey(Display, on_delete=models.CASCADE)
