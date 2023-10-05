from django.contrib import auth, messages
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def login(request):
    form=AuthenticationForm
    if request.method == "POST":
            form = AuthenticationForm(data=request.POST)
            if form.is_valid():

                print('successfuly login')
                return redirect("bankapp:status")
    else:
        form = AuthenticationForm()
    return render(request, "Login.html", {"form": form})


def register(request):
    form=UserCreationForm
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            print('successfully registered')
            return redirect("credentials:login")
    else:
        form = UserCreationForm()
    return render(request, "Register.html", {"form": form})


def logout(request):
    logout(request)
    return redirect('bankapp:demo')