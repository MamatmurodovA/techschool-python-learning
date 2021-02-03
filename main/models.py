from django.db import models

# Blog:
# Title
# Date
# Blogger
# Content


class Blog(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField()
    blogger = models.CharField(max_length=60)
    slug = models.SlugField(max_length=120, null=True)
    content = models.TextField()
    image = models.ImageField(null=True)

