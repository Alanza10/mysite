#protocolo ascii serial
#R-numero rele (1-4)-minutos(1-9)
from optparse import make_option
from django.core.management.base import BaseCommand, CommandError
from subprocess import check_output
from control.models import Riego
from django.utils import timezone
import serial
import time
from control.myserial import myserial

class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('--long', '-l', dest='long',
            help='Help for the long options'),
    )
    help = 'Help text goes here'

    def handle(self, *args, **options):
#         print "This is a command"
          ser=myserial("/dev/ttyUSB0","57600") 
          #ser.reset()
          #ser.synctime()
          if ser.enabled==1:
        	  if len(args)>=1:
        	      relay = args[0]
        	  if args[0] == '1': 
        	    ser.ser.write('R'+relay+delay)
                    r = Riego(rele='RELE1', duracion=delay, pub_date=timezone.now())
                    r.save() 
        	  elif args[0] == '2':
        	    ser.ser.write('R'+relay+delay)
                    r = Riego(rele='RELE2', duracion=delay, pub_date=timezone.now())
                    r.save()
        	  elif args[0] == '3':
        	    ser.ser.write('R'+relay+delay)
                    r = Riego(rele='RELE3', duracion=delay, pub_date=timezone.now())
                    r.save()
        	  elif args[0]== '4':
        	    ser.ser.write('R'+relay+delay)
                    r = Riego(rele='RELE4', duracion=delay, pub_date=timezone.now())
                    r.save() 
                  #time.sleep(1)       
                  #while ser.ser.inWaiting() > 0:
        	#	  data=ser.ser.readline()
                 #         print data
                    data=ser.readline()
                    print data         
                    #ser.ser.close()
       
