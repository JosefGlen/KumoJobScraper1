from django.shortcuts import render, get_object_or_404
from .models import Jobs, SavedJob
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

# Sends users to the login page if not logged in
@login_required(login_url="/users/login")
def list(request):
    query = request.GET.get("query", "")
    location = request.GET.get("location", "")

    jobs = Jobs.objects.all()

    if query:
        jobs = jobs.filter(title__icontains=query) | jobs.filter(description__icontains=query)


    if location:
        jobs = jobs.filter(location__icontains=location)

    saved_jobs = Jobs.objects.filter(savedjob__user=request.user)

    context = {
        "jobs": jobs,
        "saved_jobs": saved_jobs,
        "query": query,
        "location": location,
    }

    return render(request, "jobs/list.html", context)

@login_required(login_url="/users/login")
def page(request, id):
    # Gets the only job that matches the id
    job = Jobs.objects.get(id=id)
    return render(request, 'jobs/page.html', { 'job': job})

@login_required(login_url="/users/login")
def saved(request):
    saved_jobs = SavedJob.objects.filter(user=request.user).select_related('job')
    return render(request, 'jobs/saved.html', {'saved_jobs': saved_jobs})

@login_required
def save_job(request, job_id):
    # Prevents users from running this from the url
    if request.method == "POST":
        # Grabs the matching job within jobs or passes 404 not found error
        job = get_object_or_404(Jobs, id=job_id)
        # Creates a new instance of saved_job with the user and job as the two foreign keys
        saved_job, created = SavedJob.objects.get_or_create(user=request.user, job=job)
        #Notifies the user if the job was succesfull 
        if created:
            return JsonResponse({"message": "Job saved successfully."}, status=201)
        return JsonResponse({"message": "Job already saved."}, status=200)
    return JsonResponse({"error": "Invalid request method."}, status=400)

@login_required
def unsave_job(request, job_id):
    # Prevents users from running this from the url
    if request.method == "POST":
        # Grabs the matching job within jobs or passes 404 not found error
        job = get_object_or_404(Jobs, id=job_id)
        saved_job = SavedJob.objects.filter(user=request.user, job=job)

        #Notifies the user if the job was succesfull 
        if saved_job.exists():
            saved_job.delete()
            return JsonResponse({"message": "Job unsaved successfully."}, status=200)
        return JsonResponse({"message": "Job not found in saved list."}, status=404)
    
    return JsonResponse({"error": "Invalid request method."}, status=400)