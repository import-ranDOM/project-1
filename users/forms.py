from django import forms
from django.contrib.auth.models import User
from .models import userAccount, book


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirmPassword = forms.CharField(widget=forms.PasswordInput(), label="Confirm Password")

    # To hash the password
    def save(self, commit=True):
        User = super().save(commit=False)
        User.set_password(self.cleaned_data["password"])
        if commit:
            User.save()
        return User

    class Meta():
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')





class UserProfileForm(forms.ModelForm):

    class Meta():
        model = userAccount
        fields = ('about', 'profile_pic')
