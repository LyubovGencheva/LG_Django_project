from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from . models import Profile


# Extending the UserCreationForm to include custom fields, like e-mail
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()                          # required=True by default

    class Meta:                                         # class Meta keeps configurations in a nested place
        model = User                                    # form.save() will save it to the User model (to be affected)
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):                  # allows to username & e-mail
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):               # allows image & about update
    class Meta:
        model = Profile
        fields = ['about','image']