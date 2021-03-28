from django.contrib import admin
# from django_vuejs.apps.book.models import *
from .models import Library, Book, Author

# Register your models here.

admin.site.register(Library)
admin.site.register(Book)
admin.site.register(Author)
