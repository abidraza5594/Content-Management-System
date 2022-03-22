from django.db import models
from django.forms import EmailField

# Create your models here.
class Content(models.Model):
    name=models.CharField(max_length=20)
    phone=models.IntegerField()
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=100)
    pincode=models.IntegerField()

    def __str__(self):
        return self.name

class Contact(models.Model):
    fname=models.CharField(max_length=30)
    lname=models.CharField(max_length=30)
    email=models.EmailField()
    msg=models.TextField()
    