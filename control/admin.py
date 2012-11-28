from django.contrib import admin
from control.models import Riego

class RiegoAdmin(admin.ModelAdmin):
    fields = ['rele', 'duracion', 'pub_date']

admin.site.register(Riego, RiegoAdmin)
