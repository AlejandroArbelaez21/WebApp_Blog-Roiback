from django.db import models
from datetime import datetime

class Post(models.Model):
    categories_choices = (
        ('Python', 'Python'),
        ('Django', 'Django'),
        ('Postgresql', 'Postgresql'),
        ('HTML', 'HTML'),
        ('CSS', 'CSS'),
        ('Bootstrap', 'Bootstrap'),
        ('Backend', 'Backend'),
        ('Frontend', 'Frontend'),
        ('Full-Stack', 'Full-Stack'),
        ('JavaScript', 'JavaScript'),
        ('Web Design', 'Web Design'),
        ('Roiback', 'Roiback'),
    )

    title = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    publish_date = models.DateTimeField(default=datetime.now, blank=True)
    last_update = models.DateTimeField(auto_now=True)
    user = models.CharField(max_length=100)
    categories = models.CharField(choices=categories_choices, max_length=100, default='Other')

    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.CharField(max_length=100)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    timestap = models.DateTimeField(default=datetime.now, blank=True)
    content = models.CharField(max_length=1000)

    def __str__(self):
        return self.user

class PostView(models.Model):
    user = models.CharField(max_length=100)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    timestap = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.user

class Like(models.Model):
    user = models.CharField(max_length=100)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.user
