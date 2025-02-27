from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Jobs(models.Model):
    title = models.CharField(max_length=75)
    description = models.TextField()
    company = models.CharField(max_length=50)
    location = models.CharField(max_length=50, default="Unknown")
    salary = models.PositiveIntegerField()
    date = models.DateField(auto_now_add=True)
    slug = models.SlugField()

    def __str__(self):
        return self.title
