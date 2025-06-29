from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .models import Profile, Skill, Project, Experience, Education
from .forms import ContactForm  # We'll create this form
from django.db.models import Count

def home(request):
    profile = Profile.objects.first()
    skills = Skill.objects.all()
    projects = Project.objects.all().order_by('-date_created')
    context = {
        'profile': profile,
        'skills': skills,
        'projects': projects,
    }
    return render(request, 'portfolio/home.html', context)

def contact_view(request):
    profile = Profile.objects.first()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent successfully.")
            return redirect("home")
    else:
        form = ContactForm()
    context = {
        'profile': profile,
        'form': form,
    }
    return render(request, "portfolio/contact.html", context)
