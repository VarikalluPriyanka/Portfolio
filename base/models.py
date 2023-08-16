from django.utils import timezone
from django.db import models

#About Section

class About(models.Model):
    heading = models.CharField(max_length=50)
    career = models.CharField(max_length=20)
    description = models.TextField(blank=False)
    profile_img = models.ImageField(upload_to='profile/')
    
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.career

# Skills Section

class Category(models.Model):
    name = models.CharField(max_length=20)

    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'

    def __str__(self):
        return self.name

class Skills(models.Model):
    category = models.ForeignKey(Category,
                                on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=20)

#Certification section

class Certification(models.Model):
    title = models.CharField(max_length=100)
    issuing_organization = models.CharField(max_length=200)
    date_completed = models.DateField(default=timezone.now)
    # Add more fields as needed
    certification_link = models.URLField(default="www.google.com")

#Internship Section

class Internship(models.Model):
    title = models.CharField(max_length=100)
    issuing_organization = models.CharField(max_length=200)
    date_completed = models.DateField(default=timezone.now)
    # Add more fields as needed
    certification_link = models.URLField(default="www.google.com")
class Project(models.Model):
    title = models.CharField(max_length=100)
    description=models.TextField()
    # Add more fields as needed
    project_link = models.URLField(default="www.github.com")

#Education Section

class Education(models.Model):
    institution = models.CharField(max_length=200)
    degree = models.CharField(max_length=100)
    major = models.CharField(max_length=100)
    beginYear = models.CharField(max_length=20)
    endYear=models.CharField(max_length=20, default="2020")
    percentage=models.IntegerField(default=9)
    def __str__(self):
        return self.institution
