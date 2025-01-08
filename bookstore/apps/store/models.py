from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):

    name = models.CharField(max_length=100, help_text="Enter category Science Fiction, Horror, Thriller/Suspense, Historical Fiction, and Contemporary Fiction. etc")

    description = models.TextField()


    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    genre = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.IntegerField()

    def __str__(self):
        return self.title


class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.book.name}"

    def total_price(self):
        return self.quantity * self.book.price