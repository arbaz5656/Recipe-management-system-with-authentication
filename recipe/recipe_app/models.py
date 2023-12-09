from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class recipehome(models.Model):
    user= models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    recipename=models.CharField(max_length=100)
    recipedis=models.TextField()
    recipeimg=models.ImageField(upload_to='images/')

    def __str__(self):
        return(self.recipename)

