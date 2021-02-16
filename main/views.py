from django.http import HttpResponse
from django.shortcuts import render

from main.models import Blog, Category


def home_view(request):
    blog_with_images = Blog.objects.filter(image__isnull=False)
    context = {
        "blogs": Blog.objects.all(),
        "blog_with_images": blog_with_images,
        "categories": Category.objects.all()
    }
    return render(request=request, template_name="index.html", context=context)


def detail_view(request, slug):
    print("It's detail view")
    blog = Blog.objects.get(slug=slug)
    context = {
        "blog": blog,
        "categories": Category.objects.all()
    }
    return render(request=request, template_name="detail.html", context=context)


def category_page_view(request, category_slug):
    context = {}
    category = Category.objects.get(slug=category_slug)

    context.update({
        'categoryobj': category,
        'blogs': Blog.objects.filter(category=category),
        "categories": Category.objects.all()
    })
    return render(request=request, template_name="categories.html", context=context)
