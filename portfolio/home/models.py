from django.db import models

# Create your models here.
class Contact (models.Model):
    name = models.CharField(max_length=120)
    email = models.CharField(max_length=120)
    password = models.CharField(max_length=120)
    desc = models.TextField(max_length=120)
    date = models.DateField(max_length=120)


    def __str__(self):
        return self.name
