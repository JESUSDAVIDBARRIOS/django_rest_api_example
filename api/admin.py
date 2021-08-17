from django.contrib import admin
from .models import *

# Register your models here.

class TareaAdmin (admin.ModelAdmin):
    list_display = ("nombre", "usuario", "fecha", "completada")

admin.site.register(Tarea, TareaAdmin)
