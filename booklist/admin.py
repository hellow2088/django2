from django.contrib import admin
from .models import Author

from .models import *


class HeroAdmin(admin.ModelAdmin):
    # fieldsets = (
    #     (None, {
    #         'fields': ('id', 'name', 'skill', 'org')
    #     }),
    # )

    list_display = ['id','name','skill','org']


admin.site.register(Hero,HeroAdmin)
admin.site.register(Organization)


class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'date', 'press']
    # fields = ('id', 'title', 'writer', 'date')


admin.site.register(Book, BookAdmin)


class AuthorAdmin(admin.ModelAdmin):
    fields = ('name', 'title','birth_date')


admin.site.register(Author, AuthorAdmin)