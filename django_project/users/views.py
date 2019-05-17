from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from . forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)                               # creates the form with populated user data
        if form.is_valid():                                                 # form validation
            form.save()
            username = form.cleaned_data.get('username')                    # grabs the username from the validated form
            messages.success(request, f'Your account has been created! You are now able to log in.')   # flash message
            return redirect('login')                                        # redirects to login at successful registration
    else:
        form = UserRegisterForm()                                           # creates an empty form
    return render(request, 'users/register.html', {'form': form})           # Note: in case of unsuccessful validation,
                                                                            # the form rendered at this last statement
                                                                            # will still be populated with the (in-valid) user data


@login_required                                                             # decorator, adding functionality to existing function
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,
                                instance=request.user)                      # the form is pre-popultaed with the current user data
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)           # request.POST will save it,
                                                                            # request.FILES will save the uploaded profile pic

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your profile has been updated!')  # changed flash message
            return redirect('profile')  # redirects to login at successful registration
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)



    context = {
        'u_form': u_form,
        'p_form': p_form,
    }

    return render(request, 'users/profile.html', context)