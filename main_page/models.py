from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    added_data = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name


class Products(models.Model):
    product_name = models.CharField(max_length=60)
    product_description = models.CharField(max_length=240)
    product_price = models.FloatField()
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_amount = models.IntegerField()
    product_images = models.ImageField(upload_to='media')
    product_added_data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name


class Cart(models.Model):
    user_id = models.IntegerField()
    user_product = models.ForeignKey(Products,on_delete=models.CASCADE)
    price = models.FloatField(null=True, blank=True)
    user_cart_amount = models.IntegerField()
    cart_added_data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_id
