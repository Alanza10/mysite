from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
from GChartWrapper import *
from GChartWrapper.constants import _print
from temperaturas.models import Temperatura

def results(request):
    
    temps=Temperatura.objects.exclude(temperatura='').order_by('-pub_date')[:11]

    reverse_temps = [ temp.temperatura.rstrip() for temp in temps ] 

    reverse_temps = reverse_temps[::-1]
    #posiciones dataset    
    data1 = [0, 10, 20, 30, 40, 50 ,60 ,70, 80, 90, 100]
 
    #11 ultimas temperaturas
    data2 = reverse_temps
    
    
    # multiple axis with label positions specified
    # values between 0 and 100 - use text encoding
    data = [data1, 
           data2]
    reverse_time = [temp.pub_date.time().strftime('%H:%M') for temp in temps]
    axis2 =  reverse_time[::-1]
    
    # positions between 0 and 100
    axis = [ [0, 10, 20, 30, 40, 50 ,60 ,70, 80, 90, 100],
             axis2 ]
 

        
    # don't do integer arithmetic
    min_value = float(min(data[1]))
    max_value = float(max(data[1]))
    last_value = float(data[1][-1])
    
    G = LineXY(data, encoding='text')
    G.color('76A4FB')
    G.size(600, 240)
    G.scale('0', '100', '10', '45')
    G.marker('N*', '0077CC',0,-1,10)
    G.marker('o', '0077CC',0,-1,5)
    G.marker('r', '7fffd4',0,0.35,0.60) # 0 to 1.0
    G.axes("xyr")    
    G.axes.label(0, *axis[1])
    G.axes.position(0, *axis[0])
    G.axes.range(0, 0, 100)
    G.axes.range(1, 10, 45)
    G.axes.range(2, 10, 45)    
    G.axes.label(1, 10, 15, 20, 25, 30, 35, 40, 45)    
    G.axes.position(1, 10, 15, 20, 25, 30, 35, 40, 45) # 0 to 100
    G.axes.label(2, '%d'%last_value)
    G.axes.position(2, int(100*last_value/max_value)) # 0 to 100

    #volcar grafico en payload
    payload = {'chart_url':G}
    return render_to_response('temp/estadisticas.html', payload)

  

