from django.contrib import admin
from .models import recipehome
# Register your models here.

# admin.site.register(recipehome)


@admin.register(recipehome)
class recipehomeAdmin(admin.ModelAdmin):
    list_display = ('recipename','recipedis','recipeimg')


