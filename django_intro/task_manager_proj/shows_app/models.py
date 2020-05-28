from django.db import models
from django.db.models import Model

class ShowsManager(models.Manager): # I am trying to get caught up on my assignments so this one is not complete but I feel it best to move on to the next ones. I will continue to work on these to get them right at least for my own piece of mind.
    def validator(self,postData):
        errors = {}
        if len(postData['shows']) < 2:
            errors['shows'] = "Your title must be at least 2 characters."
        if len(postData['network']) < 3:
            errors['network'] = "Your newtwork must be at least 3 characters."
        if len(postData['desc']) < 10:
            errors['desc'] = "Your description must be at least 10 characters."
        return errors

class Shows(models.Model):
    shows = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = ShowsManager()

# Create your models here.
