from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to='products/', blank=True)

    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    ordered_date = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Order #{self.id}'


class BlogPost(models.Model):
    title = models.CharField(
        verbose_name = 'タイトル',
        max_length = 200,
    )
    
    content = models.TextField(
        verbose_name = '本文',
    )

    posted_at = models.DateTimeField(
        verbose_name = '投稿日時',
        auto_now_add = True,
    )

    category = models.ForeignKey(
        Category,
        verbose_name = 'カテゴリ',
        on_delete = models.PROTECT
    )

    def __str__(self):

        return self.title