
from django.db import models
from django.utils import timezone


class ChaipointAccount(models.Model):
    author = models.ForeignKey('auth.User')
    email = models.EmailField(max_length=200)
    mobile = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    created_date = models.DateTimeField(
            default=timezone.now)
            
    def __str__(self):
        return self.mobile,self.password