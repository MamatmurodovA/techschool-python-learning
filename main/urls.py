from django.urls import path

from main.views import home_view, detail_view, category_page_view

urlpatterns = [
    path('', home_view),
    path('categories/<slug:category_slug>', category_page_view, name='category_page'),
    path('<slug:slug>', detail_view, name='blog_detail'),
]
