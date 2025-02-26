from django.urls import path
from . import views

app_name = 'users'

# These are the urls that are called upon, views.name signifies what function will be called from the views dir
urlpatterns = [
    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
]
