#protocolo ascii serial
#R-numero rele (1-4)-minutos(1-9)
from optparse import make_option
from django.core.management.base import BaseCommand, CommandError
from subprocess import check_output
from control.models import Riego
from django.utils import timezone
import serial
import time
from control import myserial 

class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('--long', '-l', dest='long',
            help='Help for the long options'),
    )
    help = 'Help text goes here'

    def handle(self, *args, **options):
             reset()
