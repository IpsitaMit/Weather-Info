from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Gen_op(models.Model):
    name = models.CharField(max_length=50)

class Login(models.Model):
    username = models.CharField(max_length=70)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=20)

class user_list(models.Model):
    user = models.ForeignKey(User , on_delete=models.SET_NULL , null=True , blank=True)
    username=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    des=models.CharField(max_length=10, default="ull")