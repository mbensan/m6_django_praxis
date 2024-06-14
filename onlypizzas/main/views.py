from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.contrib.auth.models import User

from main.forms import RegisterForm

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

def register(req):
  form = RegisterForm()
  context = {'form': form}

  if req.method == 'GET':
    return render(req, 'registration/register.html', context)
  # en caso de POST
  form = RegisterForm(req.POST)
  if form.is_valid():
    data = form.cleaned_data
    if data['password'] != data['passRepeat']:
      messages.warning(req, "Ambas contraseñas deben coincidir")
      return redirect('/accounts/register/')
    
    User.objects.create_user(data['username'], data['email'], data['password'])
    messages.success(req, "El usuario ha sido creado con éeexito!!!")

  return redirect('/')

