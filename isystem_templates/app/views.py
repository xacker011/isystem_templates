from django.shortcuts import render
from .forms import ContactForm
from .models import *


def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def courses(request):
    posts = Courses.objects.filter(is_published=True)
    context ={
        'posts': posts
    }
    return render(request, 'courses.html', context)


def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, 'contact.html', context)
