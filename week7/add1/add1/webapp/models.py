from django.db import models


class human(models.Model):
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    phone=models.IntegerField(default=0)
    address=models.CharField(max_length=30)
    city=models.CharField(max_length=30)

# Create your models here.
