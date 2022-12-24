from django.shortcuts import render, redirect
from django.contrib.auth.forms import  AuthenticationForm
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    
    UpdateView,
    DeleteView
)
from .models import Profile
from django.urls import reverse_lazy

# view for registration
def register(req):

    if req.method == "POST":
        form = UserRegisterForm(req.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                req, f'Account created succesfully for {username}')
            return redirect('about')

    else:
        form = UserRegisterForm()
    return render(req, "users/register.html", {'form': form})

# view for login
def login(req):

    if req.method == "POST":
        form = AuthenticationForm(req, data=req.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(req, user)
                messages.success(
                    req, f'You are logged in succesfully as {username}')
                return redirect('about')
            else:
                messages.error(req, "Invalid Credentials!!")

                return redirect('about')
        else:
            messages.error(req, f"Invalid Credentials!!")

            return redirect('about')

    else:
        # to prevent user from going to login if already logged in
        if req.user.is_authenticated:
            messages.warning(req, 'You are already logged in please logout')
            return redirect('about')
        form = AuthenticationForm()
        return render(req, 'users/login.html', {"form": form})

# view for logout
def logout(req):
    auth_logout(req)
    messages.success(req, "You were succesfully logged out")
    return redirect('about')

# view for profile
@login_required
def profile(req):
    return render(req, 'users/profile.html')

# view for updating user profile (not image)
class UpdateUserProfile(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = User
    fields = ['username', 'email']
    template_name = 'users/user_form.html'
    success_url = '/profile/'

    def test_func(self):
        user = self.get_object()
        if self.request.user == user:
            return True
        return False

# view for updating user profile image
class UpdateProfileImg(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Profile
    fields = ['image']
    template_name = 'users/user_form.html'
    success_url = '/profile/'

    def test_func(self):
        profile = self.get_object()
        if self.request.user == profile.user:
            return True
        return False

# view for user delete
class UserDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = User
    # to prevent Reverse Not Found exceptions
    success_url = reverse_lazy('about')
    template_name = 'users/confirm_user_delete.html'

    def test_func(self):
        user = self.get_object()
        if self.request.user == user:
            return True
        return False


def about(req):
    return render(req, 'users/about.html')
