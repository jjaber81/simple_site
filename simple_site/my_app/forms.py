from django import forms
from django.contrib.auth.models import User
from my_app.models import UserProfileInfo

class UserForm(forms.ModelForm):
    '''
    Inherit the django user form and add to it
    '''
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username', 'email', 'password')

class UserProfileInfoForm(forms.ModelForm):
    '''
    map the UserProfile model to the form
    '''
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic')