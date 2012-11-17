from django.contrib import admin
from moisture.models import Moisture

class MoistureAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'moisture']

admin.site.register(Moisture, MoistureAdmin)
