from django.shortcuts import render, redirect
from django.contrib import messages
from . forms import UserRegisterForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)                               # creates the form with populated user data
        if form.is_valid():                                                 # form validation
            form.save()
            username = form.cleaned_data.get('username')                    # grabs the username from the validated form
            messages.success(request, f'Account created for {username}!')   # print-out success flash message (one-time alert)
            return redirect('blog-home')                                    # redirects to home after successful registration
    else:
        form = UserRegisterForm()                                           # creates an empty form
    return render(request, 'users/register.html', {'form': form})           # Note: in case of unsuccesful validation,
                                                                            # the form rendered at this last statement
                                                                            # will still be populated with the (in-valid) user data