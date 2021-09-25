from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from . import views
from django.urls import reverse_lazy

app_name = ''

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name="auth/login.html", redirect_field_name="home"), name='login'),
    path("logout", auth_views.LogoutView.as_view(), name="logout"),
    path("signup", views.SignUp.as_view(), name="signup"),
    path('home', views.home, name='home'),
    re_path('m/(?P<username>[\w-]+)/', views.ProfileDetailView.as_view(), name='profile-details'),
    re_path('(?P<username>[\w-]+)/', views.ProfileView.as_view(), name='profile'),
]
