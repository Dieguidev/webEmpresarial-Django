from django.contrib import admin
from .models import *

# Register your models here.

#*Configuracion del panel de administracion
class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

#Registrando los modelos
admin.site.register(Service, ServiceAdmin)
