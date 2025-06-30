from django.contrib import admin
from .models import Project, Experience, ContactMessage, Overview, Skill, AboutMe
from .forms import ProjectAdminForm

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'custom_name')
    search_fields = ('name', 'custom_name')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    form = ProjectAdminForm
    list_display = ('title', 'order')
    list_editable = ('order',)
    search_fields = ('title', 'description')

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('position', 'company', 'start_date', 'end_date', 'current', 'order')
    list_filter = ('current',)
    list_editable = ('order',)
    search_fields = ('position', 'company')

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'date_sent')
    search_fields = ('name', 'email', 'message')

@admin.register(Overview)
class OverviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'technical_expertise')
    search_fields = ('name', 'technical_expertise', 'bio')

@admin.register(AboutMe)
class AboutMeAdmin(admin.ModelAdmin):
    list_display = ('content',)
    search_fields = ('content',)
