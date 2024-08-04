from django.db import models


# انظر المثال هنا  User اسمها Django جاهزة في  Model الافضل استخدام
# accounts/models.py
class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    user_pic = models.ImageField(blank=True, null=True)
