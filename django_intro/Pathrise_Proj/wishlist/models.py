from django.db import models

class Wish(models.Model):
    name = models.CharField(max_length=45)
    job = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Create your models here.
