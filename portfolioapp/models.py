from django.db import models

class PersonalInfo(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    email = models.EmailField()
    profile_picture = models.ImageField(upload_to='profile_pics/')

    def __str__(self):
        return self.name

class Technology(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    tech_stack = models.ManyToManyField(Technology)  # Many-to-Many for tech stack
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)  # Optional end date
    link = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='project_images/', blank=True, null=True)

    def __str__(self):
        return self.title