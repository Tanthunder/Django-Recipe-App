from pickle import TRUE
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    author = models.ForeignKey(User,on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=TRUE)
    updated_at = models.DateTimeField(auto_now=TRUE)
    
    def get_absolute_url(self):
      return reverse('recipes-detail', kwargs={'pk':self.pk})

    def __str__(self):
      return self.title
