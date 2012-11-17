import datetime
from django.db import models

# Create your models here.

class Temperatura(models.Model):
    temperatura = models.CharField(max_length=200)
    pub_date = models.DateTimeField('fecha temperatura')

    def __unicode__(self):
        return self.temperatura
    def fecha(self):
        return self.pub_date
