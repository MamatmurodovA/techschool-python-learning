from django.http import HttpResponse
from django.shortcuts import render

from main.models import Blog


def home_view(request):
    blog_with_images = Blog.objects.filter(image__isnull=False)
    context = {
        "blogs": Blog.objects.all(),
        "blog_with_images": blog_with_images
    }
    return render(request=request, template_name="index.html", context=context)


def detail_view(request, slug):
    print("It's detail view")
    blog = Blog.objects.get(slug=slug)
    context = {
        "blog": blog
    }
    return render(request=request, template_name="detail.html", context=context)

