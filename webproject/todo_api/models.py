from tkinter import CASCADE
from django.db import models
from django.forms import CharField
from core.models import UserProfileModel

# Create your models here.
class TODOModel(models.Model):
    """ TODO Model """

    id = models.AutoField(auto_created=True,primary_key=True)
    user = models.ForeignKey(UserProfileModel,on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    date = models.DateField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)