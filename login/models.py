from django.db import models

class Login(models.Model):
    username=models.CharField(max_length=15)
    password=models.CharField(max_length=10)

    def __str__(self):
        return self.username

class Register(models.Model):
    name=models.CharField(max_length=20)
    username=models.CharField(max_length=15)
    email=models.CharField(max_length=50)
    mobile=models.IntegerField()
    password=models.CharField(max_length=10)

    def __str__(self):
        return self.username

class Image(models.Model):
    imgfile=models.ImageField(upload_to='images')


class Contact(models.Model):
    phone=models.IntegerField()
    message=models.CharField(max_length=100)