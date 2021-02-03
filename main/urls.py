from django.urls import path

from main.views import home_view, detail_view

urlpatterns = [
    path('', home_view),
    path('<slug:slug>', detail_view, name='blog_detail'),
]
