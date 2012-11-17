#protocolo ascii serial
#R-numero rele (1-4)-minutos(1-9)
#No usar de momento
from optparse import make_option
from django.core.management.base import BaseCommand, CommandError
from subprocess import check_output
from control.models import Riego
from django.utils import timezone
import serial
import time

class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('--long', '-l', dest='long',
            help='Help for the long options'),
    )
    help = 'Help text goes here'

    def handle(self, *args, **options):
#         print "This is a command"
	  ser = serial.Serial('/dev/ttyUSB0', 9600)
# Por defecto delay 1 si hay segundo parametro se cambia          
	  delay = '1'
          
	  if len(args)==2:
	      delay = args[1]
# Por defecto relay 1 se cambia por primer parametro          
	  relay = '1'
	  if len(args)>=1:
	      relay = args[0]
	  if args[0] == '1': 
	    ser.write('R'+relay+delay)
            r = Riego(rele='RELE1', duracion=delay, pub_date=timezone.now())
            r.save() 
	  elif args[0] == '2':
	    ser.write('R'+relay+delay)
            r = Riego(rele='RELE2', duracion=delay, pub_date=timezone.now())
            r.save()
	  elif args[0] == '3':
	    ser.write('R'+relay+delay)
            r = Riego(rele='RELE3', duracion=delay, pub_date=timezone.now())
            r.save()
	  elif args[0]== '4':
	    ser.write('R'+relay+delay)
            r = Riego(rele='RELE4', duracion=delay, pub_date=timezone.now())
            r.save() 
          time.sleep(1)       
          while ser.inWaiting() > 0:
		  data=ser.readline()
                  print data
          ser.close()
   
