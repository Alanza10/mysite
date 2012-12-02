from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
from GChartWrapper import *
from GChartWrapper.constants import _print
from temperaturas.models import Temperatura

def results(request):
    
    temps=Temperatura.objects.order_by('-pub_date')[:10]
 

    data1 = [2, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57, 61, 65, 69, 73, 79, 83, 87, 91, 95 ]
    
    data2 =  [25, 24, 25, 23.5, 25, 24, 24, 24.5]
    
    # multiple axis with label positions specified
    # values between 0 and 100 - use text encoding
    data = [data1, 
           data2]
    
    # positions between 0 and 100
    axis = [ [2, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57, 61, 65, 69, 73, 79, 83, 87, 91, 95 ],
             ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12',
            '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '00'] ]
 

        
    # don't do integer arithmetic
    min_value = float(min(data[1]))
    max_value = float(max(data[1]))
    last_value = float(data[1][-1])
    
    G = LineXY(data, encoding='text')
    G.color('76A4FB')
    G.size(600, 240)
    G.scale('0', '100', '10', '45')
    G.marker('o', '0077CC',0,-1,5)
    G.marker('r', '7fffd4',0,0.35,0.60) # 0 to 1.0
    G.axes("xyr")    
    G.axes.label(0, *axis[1])
    G.axes.position(0, *axis[0])
    G.axes.range(0, 0, 100)
    G.axes.range(1, 10, 45)  
    G.axes.label(1, 10, 15, 20, 25, 30, 35, 40, 45)    
    G.axes.position(1, 10, 15, 20, 25, 30, 35, 40, 45) # 0 to 100
    G.axes.label(2, '%d'%last_value)
    G.axes.position(2, int(100*last_value/max_value)) # 0 to 100

    #volcar grafico en payload
    chart_url=G
    payload = {'chart_url':G}
    return render_to_response('temp/estadisticas.html', payload)

  

