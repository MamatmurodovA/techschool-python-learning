from django.contrib import admin

from main.models import Blog, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'position', )
    ordering = ('position', )


class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date', 'blogger')


admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)


