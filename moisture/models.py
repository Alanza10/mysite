import datetime
from django.db import models

# Create your models here.

class Moisture(models.Model):
    moisture = models.CharField(max_length=4)
    pub_date = models.DateTimeField('fecha humedad')

    def __unicode__(self):
        return self.moisture
 #   def fecha(self):
 #       return self.pub_date
