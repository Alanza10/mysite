import datetime, qsstats
from optparse import make_option
from django.core.management.base import BaseCommand, CommandError
from temperaturas.models import Temperatura

class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('--long', '-l', dest='long',
            help='Help for the long options'),
    )

    help = 'Help text goes here'

    def handle(self, **options):    
        qs = Temperatura.objects.all()
        qss = qsstats.QuerySetStats(qs, 'temperaturas_temperatura')
        
        today = datetime.date.today()
        seven_days_ago = today - datetime.timedelta(days=7)
        
        time_series = qss.time_series(seven_days_ago, today)
        print 'New users in the last 7 days: %s' % [t[1] for t in time_series]
