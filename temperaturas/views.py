from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist


from pygooglechart import PieChart2D

def results():
    chart = PieChart2D(400, 200)
    chart.set_pie_labels("sss")
    chart_url = chart.get_url()
    payload = {'question':question, 'total_votes':total_votes, 'chart_url':chart_url}
    return render('temp/estadisticas.html', payload)

  

