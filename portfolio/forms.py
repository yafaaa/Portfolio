from django import forms
from .models import ContactMessage, Project, Skill

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ["name", "email", "message"]

class ProjectAdminForm(forms.ModelForm):
    skills = forms.ModelMultipleChoiceField(
        queryset=Skill.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Skills/Frameworks",
        help_text="Select one or more skills or frameworks for this project."
    )
    class Meta:
        model = Project
        fields = ['title', 'description', 'image', 'live_demo_link', 'github_link', 'order', 'skills']
