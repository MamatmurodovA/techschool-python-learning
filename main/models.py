from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255)
    position = models.IntegerField(default=1)
    slug = models.SlugField(max_length=120)

    def __str__(self):
        return self.title


class Blog(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField()
    blogger = models.CharField(max_length=60)
    slug = models.SlugField(max_length=120, null=True)
    content = models.TextField()
    image = models.ImageField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title
