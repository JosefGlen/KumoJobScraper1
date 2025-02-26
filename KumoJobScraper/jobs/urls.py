from django.urls import path
from . import views

app_name = 'jobs'

urlpatterns = [
    path('', views.jobs_list, name="list"),
    path('jobs_saved/', views.jobs_saved, name="saved"),
    path('<slug:slug>', views.job_page, name="page"),
]
