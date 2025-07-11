# Generated by Django 5.2.3 on 2025-06-29 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_delete_education_delete_profile_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skill',
            name='category',
        ),
        migrations.AlterModelOptions(
            name='skill',
            options={'ordering': ['order', 'name']},
        ),
        migrations.RemoveField(
            model_name='skill',
            name='proficiency_percentage',
        ),
        migrations.AddField(
            model_name='skill',
            name='order',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='skill',
            name='proficiency',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.DeleteModel(
            name='SkillCategory',
        ),
    ]
