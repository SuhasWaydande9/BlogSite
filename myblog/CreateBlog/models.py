from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Blog(models.Model):
    def __str__(self):
        return self.title

    title = models.CharField(max_length = 40)
    story = models.TextField(default='')
    categoryChoices = (
        ('comedy','comedy'),
        ('romantic', 'romantic'),
        ('mystery', 'mystery'),
        ('horror', 'horror'),
        ('mythology', 'mythology'),
        ('normal', 'normal')
    )
    category = models.CharField(max_length=30, choices = categoryChoices, 
        default = 'normal')
    DateTime = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Blog_User')
    


