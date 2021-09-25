from django.shortcuts import render, get_object_or_404
from .forms import UserForm, UserProfileForm

from django.contrib.auth import login, logout, views
from django.urls import reverse_lazy
from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView, View)

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    return render(request, 'home.html')

################################# SIGN UP VIEW ####################################
class SignUp(CreateView):
    form_class = UserForm
    success_url = reverse_lazy("home")
    template_name = "auth/signup.html"

###################################################################################





########################## Logged In User Profile VIEW #################################
class ProfileDetailView(LoginRequiredMixin, View):
    template_name = 'profile/profile_details.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

#######################################################################################





################################### GENERAL USER PROFILE VIEW ##############################
class ProfileView(DetailView):
    template_name = 'profile/view_profile.html'

    def get_object(self):
        username = self.kwargs.get("username")
        if username is None:
            raise Http404
        return get_object_or_404(User, username__iexact=username, is_active=True)

#############################################################################################
