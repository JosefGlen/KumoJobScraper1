from django.shortcuts import render, get_object_or_404
from .models import Jobs, SavedJob
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse


# Create your views here.
# Sends users to the login page
@login_required(login_url="/users/login")
def list(request):
    jobs = Jobs.objects.all()  # Fetch all jobs
    saved_jobs = Jobs.objects.filter(savedjob__user=request.user)  # Only jobs saved by this user
    
    return render(request, "jobs/list.html", {"jobs": jobs, "saved_jobs": saved_jobs})

@login_required(login_url="/users/login")
def page(request, id):
    # Gets the only job that matches the slug
    job = Jobs.objects.get(id=id)
    return render(request, 'jobs/page.html', { 'job': job})

@login_required(login_url="/users/login")
def saved(request):
    saved_jobs = SavedJob.objects.filter(user=request.user).select_related('job')
    return render(request, 'jobs/saved.html', {'saved_jobs': saved_jobs})

@login_required
def save_job(request, job_id):
    if request.method == "POST":
        job = get_object_or_404(Jobs, id=job_id)
        saved_job, created = SavedJob.objects.get_or_create(user=request.user, job=job)

        if created:
            return JsonResponse({"message": "Job saved successfully."}, status=201)
        return JsonResponse({"message": "Job already saved."}, status=200)
    return JsonResponse({"error": "Invalid request method."}, status=400)

@login_required
def unsave_job(request, job_id):
    if request.method == "POST":
        job = get_object_or_404(Jobs, id=job_id)
        saved_job = SavedJob.objects.filter(user=request.user, job=job)

        if saved_job.exists():
            saved_job.delete()
            return JsonResponse({"message": "Job unsaved successfully."}, status=200)
        return JsonResponse({"message": "Job not found in saved list."}, status=404)
    
    return JsonResponse({"error": "Invalid request method."}, status=400)