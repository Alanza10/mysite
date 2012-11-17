from optparse import make_option
from django.core.management.base import BaseCommand, CommandError
from subprocess import check_output
from temperaturas.models import Temperatura
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

    def handle(self, **options):
#         print "This is a command"
          ser=myserial("/dev/ttyUSB0","57600") 
          ser.synctime() 
          data = ser.date()          
          ser.ser.close()
          if data:
             print data
          else:
             print "No"
         
