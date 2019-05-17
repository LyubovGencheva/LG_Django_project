from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from . forms import UserRegisterForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)                               # creates the form with populated user data
        if form.is_valid():                                                 # form validation
            form.save()
            username = form.cleaned_data.get('username')                    # grabs the username from the validated form
            messages.success(request, f'Your account has been created! You are now able to log in.')   # changed flash message
            return redirect('login')                                        # redirects to login at successful registration
    else:
        form = UserRegisterForm()                                           # creates an empty form
    return render(request, 'users/register.html', {'form': form})           # Note: in case of unsuccesful validation,
                                                                            # the form rendered at this last statement
                                                                            # will still be populated with the (in-valid) user data

@login_required                                                             # decorator, adding functionality to existing function
def profile(request):
    return render(request, 'users/profile.html')