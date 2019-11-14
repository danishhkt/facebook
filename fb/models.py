from django.db import models

# Create your models here.
class login(models.model):
    email =models.Charfield(max_length=25)
    password=models.Charfield(max_length=25)
class Register(models.model):
    firstname=models.Charfield(max_length=25)
    surname=models.Charfield(max_length=25)
    birthday=models.Datafield()
    gender=models.Charfield(max_length=25)
    fk_login=models.ForeignKey(Login,on_delete=models.CASCADE)