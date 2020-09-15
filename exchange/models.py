from django.db import models
# Create your models here.


class Question(models.Model):
    q = models.CharField(max_length=200)
    a = models.CharField(max_length=200)
    title = models.CharField(max_length=50)


class People(models.Model):
    uname = models.CharField(max_length=20)
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    password = models.CharField(max_length=20)


class Answers(models.Model):
    a = models.CharField(max_length=300)
    num = models.IntegerField()
