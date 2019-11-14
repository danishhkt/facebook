from django.db import models

# Create your models here.
class login(models.Model):
    email =models.CharField(max_length=25)
    password=models.CharField(max_length=25)
class Register(models.Model):
    firstname=models.CharField(max_length=25)
    surname=models.CharField(max_length=25)
    birthday=models.DateField()
    gender=models.CharField(max_length=25)
    fk_login=models.ForeignKey(login,on_delete=models.CASCADE)