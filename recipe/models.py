from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from datetime import datetime


class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe_name = models.CharField(max_length=200)
    ingredients = models.TextField()
    method_of_preparation = models.TextField()
    time_of_preparation = models.IntegerField()
    serves = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    recipe_date = models.DateField(default=datetime.now, blank=True)
    recipe_image = models.ImageField(upload_to='photos/%d/%m/Y/', blank=True)
    published = models.BooleanField(default=False)
    
    def __str__(self):
        return self.recipe_name
