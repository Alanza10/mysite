from optparse import make_option
from django.core.management.base import BaseCommand, CommandError
from subprocess import check_output
from temperaturas.models import Temperatura
from django.utils import timezone

class Command(BaseCommand):
  option_list = BaseCommand.option_list + (
  make_option('--long', '-l', dest='long',
    help='Help for the long options'),)
    
  help = 'Help text goes here'

  def handle(self, **options):
    #    print "This is a command"
#         s=check_output('temper', shell=True)
    s = check_output('sudo temper | grep -o "[0-9]\{1,3\}\.[0-9]\{1,3\}C" | grep -o "[0-9]\{1,3\}\.[0-9]\{1,3\}"', shell=True)
    unicodes = unicode(s,"utf-8")
    t=Temperatura(temperatura=unicodes, pub_date=timezone.now())
    t.save() 
    print unicodes
