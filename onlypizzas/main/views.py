from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView

class LoginViewPropia(SuccessMessageMixin, LoginView):
  success_message = "Has ingresado correctamente"

# Create your views here.
def index(req):
  return render(req, 'index.html')


def about(req):
  return render(req, 'about.html')

@login_required
def welcome(req):
  return render(req, 'welcome.html')


def contact(req):
  return render(req, 'contact.html')


