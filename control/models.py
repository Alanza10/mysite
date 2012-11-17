import datetime
from django.db import models

# Create your models here.

class Riego(models.Model):
    rele = models.CharField(max_length=5)
    duracion = models.CharField(max_length=1)
    pub_date = models.DateTimeField('fecha riego')

    def __unicode__(self):
        return self.rele
        

    def __unicode__(self):
        return self.rele
       
    def fecha(self):
        return self.pub_date
