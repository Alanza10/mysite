from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
from GChartWrapper import *
from GChartWrapper.constants import _print

from pygooglechart import PieChart2D

def results(request):
    # Add red line 6 thick
    # with 5 line segments with 2 blank segments
    G = Line( ['hX1xPj'] )
    G.axes('xy')
    G.axes.label(0, 'Mar', 'Apr', 'May', 'June', 'July')
    G.axes.label(1, None, '50+Kb')        
    G.color('red')
    G.line(6,5,2)
    _print('prueba','\t',G)
    chart_url=G
    print "url"
    print chart_url
    payload = {'chart_url':G}
    return render_to_response('temp/estadisticas.html', payload)

  

