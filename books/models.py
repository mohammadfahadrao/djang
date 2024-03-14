from django.db import models

# Create your models here.

class Questions(models.Model):
    
    def __str__(self):
        return self.publisher_email

    publisher_email = models.EmailField()
    publisher_name = models.TextField(max_length=200)

class Something(models.Model):
    def __str__(self) -> str:
        return self.some_column
    some_column = models.BooleanField(True)