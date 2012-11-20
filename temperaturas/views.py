from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth import User
import datetime
import qsstats

def estadisticas(request):

    GOOGLE_API_KEY = 'clave'

    qs = User.objects.all()
    qss = qsstats.QuerySetStats(qs, 'temperaturas_temperatura')

    hoy = datetime.date.today()
    hace_2_semanas = hoy - datetime.timedelta(weeks=2)

    users_stats = qss.time_series(hace_2_semanas, hoy)

    return render_to_response('estadisticas.html', locals(), context_instance=RequestContext(request))




  

