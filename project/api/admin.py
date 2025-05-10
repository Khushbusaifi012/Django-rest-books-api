from django.contrib import admin
from api.models import Book

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display=['title','author','published_date']

admin.site.register(Book,BookAdmin)