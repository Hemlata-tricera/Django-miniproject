from django.db import models

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


