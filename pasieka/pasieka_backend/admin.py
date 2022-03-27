from django.contrib import admin
from .models import Beehive
# Register your models here.


@admin.register(Beehive)
class BeehiveAdmin(admin.ModelAdmin):
    pass
