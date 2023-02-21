from django.db import models

# Create your models here.

class Member(models.Model):
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=12)

    def __str__(self):
        return self.username