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
    
class SavedJob(models.Model):
    # On Delete of either User or Job, all associated objects will also be Deleted
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Jobs, on_delete=models.CASCADE)
    saved_on = models.DateTimeField(auto_now_add=True)

    # Makes it so that users can't save the same job multiple times
    class Meta:
        unique_together = ('user', 'job')

    def __str__(self):
        return f"{self.user.username} - {self.job.title}"