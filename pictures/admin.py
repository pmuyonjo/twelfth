from django.contrib import admin
from .models import Pictures


class PicturesAdmin(admin.ModelAdmin):
    list_display = ('name', 'banner')


admin.site.register(Pictures,PicturesAdmin)
# Register your models here.
