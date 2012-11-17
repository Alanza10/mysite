from optparse import make_option
from django.core.management.base import BaseCommand, CommandError
from subprocess import check_output
from moisture.models import Moisture
from django.utils import timezone
import serial
import re
from control.myserial import myserial
import time

class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('--long', '-l', dest='long',
            help='Help for the long options'),
    )
    help = 'Help text goes here'

    def handle(self, **options):
#         print "This is a command"
          ser=myserial("/dev/ttyUSB0","57600") 
          ser.synctime() 
          data = ser.humedad()          
          ser.ser.close()
          m = re.match(r'Soil moisture: (.*)', data)
          if m:
	     unicodes=unicode(m.group(1), "utf-8")
             moisture = Moisture(moisture=unicodes, pub_date=timezone.now())
	     moisture.save()
             print unicodes
          else:
             print "No se puede leer humedad"
         

       

