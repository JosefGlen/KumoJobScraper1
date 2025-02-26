from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# Pseudonyms used because the functions are of the same name
from django.contrib.auth import login as lgIN, logout as lgOUT

def register(request):
    if request.method == "POST":
        # Creates a form with the returned information
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # If the form is valid it saves as a new user
            lgIN(request, form.save())
            # Redirects you to the jobs list if succesfull
            return redirect("jobs:list")
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', { 'form': form })

# Checks if the login page was brought to by the login page
def login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        # Checks if the login data was correct
        if form.is_valid():
            lgIN(request, form.get_user())
            # Redirects to the jobs list page upon login, may swap with homepage
            return redirect("jobs:list")
    else:
        # Creates a login form
        form = AuthenticationForm()
    return render(request, 'users/login.html', { 'form': form })

# Logs the user out
def logout(request):
    if request.method == "POST":
        lgOUT(request)
        # Takes them to the homepage
        return redirect("/")
    return request