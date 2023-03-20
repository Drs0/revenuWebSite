from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import * 
from datetime import datetime
# Create your models here.


class Mailer(AbstractUser):
    username = models.CharField(unique=True,max_length=30)
    name = models.CharField(max_length=40)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name']
    class Meta:
        db_table = "Mailer"

class dailyGoal(models.Model):
    goal=models.IntegerField(default=0)
    dayOfMonth = models.IntegerField(default=datetime.now().strftime('%d'))
    Day= models.CharField(default=datetime.now().strftime('%A'),max_length=30)
    Month= models.CharField(default=datetime.now().strftime('%B'),max_length=30)
    Year= models.IntegerField(default=datetime.now().strftime('%Y'))
    mailer= models.ForeignKey(Mailer,on_delete=models.CASCADE)
    class Meta:
        db_table = "Goal"

