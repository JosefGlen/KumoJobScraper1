from django.urls import path
from . import views

app_name = 'jobs'

urlpatterns = [
    path('', views.list, name="list"),
    path('saved/', views.saved, name="saved"),
    path('save-job/<int:job_id>/', views.save_job, name='save_job'),
    path('unsave-job/<int:job_id>/', views.unsave_job, name='unsave_job'),
    path('<int:id>', views.page, name="page"),
]
