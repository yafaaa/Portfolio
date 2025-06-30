from django.db import models

class Skill(models.Model):
    SKILL_CHOICES = [
        ("Python", "Python"),
        ("Java", "Java"),
        ("JavaScript", "JavaScript"),
        ("TypeScript", "TypeScript"),
        ("C", "C"),
        ("C++", "C++"),
        ("C#", "C#"),
        ("Go", "Go"),
        ("Rust", "Rust"),
        ("Ruby", "Ruby"),
        ("PHP", "PHP"),
        ("Swift", "Swift"),
        ("Kotlin", "Kotlin"),
        ("Scala", "Scala"),
        ("Dart", "Dart"),
        ("Objective-C", "Objective-C"),
        ("Perl", "Perl"),
        ("R", "R"),
        ("MATLAB", "MATLAB"),
        ("SQL", "SQL"),
        ("HTML", "HTML"),
        ("CSS", "CSS"),
        ("React", "React"),
        ("Vue.js", "Vue.js"),
        ("Angular", "Angular"),
        ("Django", "Django"),
        ("Flask", "Flask"),
        ("Spring", "Spring"),
        ("Express.js", "Express.js"),
        ("Laravel", "Laravel"),
        (".NET", ".NET"),
        ("Node.js", "Node.js"),
    ]
    name = models.CharField(max_length=100, choices=SKILL_CHOICES, blank=True)
    custom_name = models.CharField(max_length=100, blank=True, help_text="If not in the list, enter a custom skill or framework.")
    
    def __str__(self):
        return self.custom_name if self.custom_name else self.name

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='project_images/')
    live_demo_link = models.URLField(blank=True, null=True)
    github_link = models.URLField(blank=True)
    order = models.PositiveIntegerField(default=0)
    skills = models.ManyToManyField(Skill, blank=True, related_name='projects')
    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order', 'title']

class Experience(models.Model):
    company = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    current = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return f"{self.position} at {self.company}"
    
    class Meta:
        ordering = ['order', '-start_date']

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    date_sent = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Message from {self.name}"
    
    class Meta:
        ordering = ['-date_sent']

class Overview(models.Model):
    name = models.CharField(max_length=200)
    technical_expertise = models.CharField(max_length=200)
    bio = models.TextField()
    
    def __str__(self):
        return self.name

class AboutMe(models.Model):
    content = models.TextField(help_text="Enter the About Me text.")

    def __str__(self):
        return "About Me"

    class Meta:
        verbose_name = "About Me"
        verbose_name_plural = "About Me"
