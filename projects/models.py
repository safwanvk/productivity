from django.db import models

from users.models import User



# Create your models here.
class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(default='', blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)