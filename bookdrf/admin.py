from django.contrib import admin

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