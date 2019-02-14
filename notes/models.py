from django.db import models
from django.utils import timezone
# Create your models here.


class Type(models.Model):
    title = models.CharField(max_length=8)

    def __str__(self):
        return self.title


class Note(models.Model):
    title = models.CharField(max_length=40)
    body = models.TextField(max_length=1200)
    status = models.ForeignKey(Type, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title
