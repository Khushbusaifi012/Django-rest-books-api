from django.db import models

# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=30)
    author=models.CharField(max_length=20)
    published_date=models.DateField()

    def __str__(self):
        return self.title
    
