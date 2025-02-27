from django.contrib import admin
from .models import Jobs, SavedJob

# Register your models here.

admin.site.register(Jobs)
admin.site.register(SavedJob)
