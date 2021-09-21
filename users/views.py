from django.shortcuts import render
from .forms import UserForm, UserProfileForm

from django.contrib.auth import login, logout, views
from django.urls import reverse_lazy
from django.views.generic import CreateView

# Create your views here.

class SignUp(CreateView):
    form_class = UserForm
    success_url = reverse_lazy("home")
    template_name = "auth/signup.html"


def profile_view(request):
    return render(request, 'auth/profile_detail.html')

def home(request):
    return render(request, 'home.html')
