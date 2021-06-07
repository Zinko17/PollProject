from django.contrib.auth.models import User
from django.db import models
from .forms import *

class Poll(models.Model):
    title = models.CharField(max_length=70,default=None)
    user = models.ForeignKey(User,on_delete=models.CASCADE)


class Question(models.Model):
    poll = models.ForeignKey(Poll,on_delete=models.SET_NULL,null=True,related_name='quest')
    text = models.CharField(max_length=70)
    answer = models.CharField(max_length=20)


