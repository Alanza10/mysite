from django.contrib import admin
from temperaturas.models import Temperatura

class TemperaturaAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'temperatura']

admin.site.register(Temperatura, TemperaturaAdmin)
