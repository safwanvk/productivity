from django.db import models

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
    fb_profile = models.CharField(max_length=255)
    twitter_profile = models.CharField(max_length=255)
    linkedin_profile = models.CharField(max_length=255)
    website = models.CharField(max_length=255)
    objects = models.Manager()

    def __str__(self):
        return self.name
