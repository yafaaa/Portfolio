from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Project, Experience, Overview, AboutMe  # Added AboutMe import
from .forms import ContactForm


def home(request):
    overview = Overview.objects.first()
    aboutme = AboutMe.objects.first()
    # Removed skills = Skill.objects.all()
    projects = Project.objects.all()  # Use default Meta ordering (order, title)
    experiences = Experience.objects.all().order_by('order', '-start_date')
    context = {
        'overview': overview,
        'aboutme': aboutme,
        # 'skills': skills,  # Removed
        'projects': projects,
        'experiences': experiences,
    }
    return render(request, 'portfolio/home.html', context)


def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent successfully.")
            return redirect("home")
    else:
        form = ContactForm()
    context = {
        'form': form,
    }
    return render(request, "portfolio/contact.html", context)
