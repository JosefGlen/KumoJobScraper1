from django.urls import path
from . import views

app_name = 'jobs'

urlpatterns = [
    path('', views.list, name="list"),
    path('saved/', views.saved, name="saved"),
    # Calls the appropriate functions in the views folder, passes the job id as an argument
    path('save-job/<int:job_id>/', views.save_job, name='save_job'),
    path('unsave-job/<int:job_id>/', views.unsave_job, name='unsave_job'),
    # Uses the Jobs ID for the slug of the page
    path('<int:id>', views.page, name="page"),
]
