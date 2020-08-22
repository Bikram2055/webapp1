from django.db import models


# Create your models here.
class login(models.Model):
    username = models.CharField(max_length=40)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=20)
    phone = models.IntegerField()


class menu_item(models.Model):
    image = models.ImageField()
    price = models.IntegerField()
    name = models.CharField(max_length=40)
    describe = models.CharField(max_length=200)
