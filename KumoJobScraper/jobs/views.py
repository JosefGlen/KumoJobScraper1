from django.shortcuts import render
from .models import Jobs
from django.contrib.auth.decorators import login_required

# Create your views here.
# Sends users to the login page
@login_required(login_url="/users/login")
def jobs_list(request):
    # Grabs all of the jobs
    jobs = Jobs.objects.all().order_by('-date')
    return render(request, 'jobs/jobs_list.html', { 'jobs': jobs})

def job_page(request, slug):
    # Gets the only job that matches the slug
    job = Jobs.objects.get(slug=slug)
    return render(request, 'jobs/job_page.html', { 'job': job})

def jobs_saved(request):
    return render(request, 'jobs/jobs_saved.html')
