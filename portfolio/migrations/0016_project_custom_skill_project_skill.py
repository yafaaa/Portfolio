# Generated by Django 5.2.3 on 2025-06-29 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0015_remove_project_technologies'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='custom_skill',
            field=models.CharField(blank=True, help_text='If not in the list, enter a custom skill.', max_length=100),
        ),
        migrations.AddField(
            model_name='project',
            name='skill',
            field=models.CharField(blank=True, choices=[('Python', 'Python'), ('Java', 'Java'), ('JavaScript', 'JavaScript'), ('TypeScript', 'TypeScript'), ('C', 'C'), ('C++', 'C++'), ('C#', 'C#'), ('Go', 'Go'), ('Rust', 'Rust'), ('Ruby', 'Ruby'), ('PHP', 'PHP'), ('Swift', 'Swift'), ('Kotlin', 'Kotlin'), ('Scala', 'Scala'), ('Dart', 'Dart'), ('Objective-C', 'Objective-C'), ('Perl', 'Perl'), ('R', 'R'), ('MATLAB', 'MATLAB'), ('SQL', 'SQL'), ('HTML', 'HTML'), ('CSS', 'CSS'), ('React', 'React'), ('Vue.js', 'Vue.js'), ('Angular', 'Angular'), ('Django', 'Django'), ('Flask', 'Flask'), ('Spring', 'Spring'), ('Express.js', 'Express.js'), ('Laravel', 'Laravel'), ('.NET', '.NET'), ('Node.js', 'Node.js')], help_text='Choose from the list or enter a new skill.', max_length=100),
        ),
    ]
