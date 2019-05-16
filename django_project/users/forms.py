from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# Extending the UserCreationForm to include custom fields, like e-mail
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()                          # required=True by default

    class Meta:                                         # class Meta keeps configurations in a nested place
        model = User                                    # form.save() will save it to the USer model (to be affected)
        fields = ['username', 'email', 'password1', 'password2']
