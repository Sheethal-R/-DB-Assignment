from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    product_id =models.PositiveIntegerField(max_length=200)
    product_name = models.CharField(max_length=100)
    category_id=models.ForeignKey(User,on_delete=models.CASCADE,)
    price=models.DecimalField(decimal_places=2,max_digits=10)
    
    def __str__(self) -> str:
        return self. product_id 
    
class Product_category(models.Model):
    category_id=models.PositiveIntegerField(max_length=200)
    category_name =models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.category_id 
    

    

    

