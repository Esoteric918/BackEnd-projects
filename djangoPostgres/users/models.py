from django.db import models

# Create your models here.

class Course(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)

    def __str__(self):
        return self.summary

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=80)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=1500)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + " " + self.content



