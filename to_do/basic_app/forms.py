from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from basic_app.models import UserProfile

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text="Enter a valid email address")
    class Meta:
        model = User
        fields = ['username', 'email']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['portfolio_site']