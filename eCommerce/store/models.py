from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=30, unique=True)
    price = models.FloatField()
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='seller')
    description = models.TextField(max_length=10000)
    image = models.ImageField(upload_to='images', blank=True)

    def __str__(self):
        return self.name
    
    def split_description(self):
        return self.description.split('\n')

class Order(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='product')
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='buyer')
    date = models.DateField(auto_now_add=True, editable=False, blank=True)

    def __str__(self):
        return f'{self.product}: {self.buyer}'