from django.db import models

# Create your models here.


class Type(models.Model):
    title = models.CharField(max_length=8)

    def __str__(self):
        return self.title


class Note(models.Model):
    date = models.DateField()
    title = models.CharField(max_length=40)
    body = models.TextField(max_length= 1200)

    def __str__(self):
        return self.title