from django.shortcuts import render
from django.http import HttpResponse
import random
from string import ascii_lowercase, ascii_uppercase
# Create your views here.
def home(request):
    return render(request, 'generator/home.html')

def password(request):
    thepassword = ''
    characters = ascii_lowercase
    length = int(request.GET.get('length', 12))
    if request.GET.get('uppercase'):
        characters += ascii_uppercase
    if request.GET.get('special'):
        characters += '!@#$%^&*()_+|=-' 
    if request.GET.get('numbers'):
        characters += '0123456789'        
    for x in range(length):
        thepassword += random.choice(characters)
    return render(request, 'generator/password.html', {'password': thepassword})

def about_me(request):
    return render(request, 'generator/aboutme.html',)