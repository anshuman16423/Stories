from django.db import models

class User(models.Model):
    username = models.CharField(max_length=25,primary_key=True)
    password = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
