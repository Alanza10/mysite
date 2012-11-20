from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *
from django.views.generic import ListView
from control.models import Riego
#from django.views.generic.simple import direct_to_template
from django.contrib import admin
#from jsonrpc import jsonrpc_site
import temperaturas.views
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^polls/', include('polls.urls')),
    url(r'^control/', include('control.urls')),
    url(r'', include('control.urls')),
    url(r'^temp/', include('temperaturas.urls')),
 #   url(r'^temp2/',  TemplateView.as_view(template_name='estadisticas.html')),
    url(r'^mois/', include('moisture.urls')),
    url(r'^riegos/',ListView.as_view(
            queryset=Riego.objects.order_by('-pub_date'),
            context_object_name='latest_riego_list',
            template_name='riegos/index.html'),
            name='riegos_index'),
    url(r'^admin/', include(admin.site.urls)),
#  url(r'^json/browse/', 'jsonrpc.views.browse', name="jsonrpc_browser"), # for the graphical browser/web console only, omissible
 # url(r'^json/', jsonrpc_site.dispatch, name="jsonrpc_mountpoint"),
#  (r'^json/(?P<method>[a-zA-Z0-9.]+)$', jsonrpc_site.dispatch) # for HTTP GET only, also omissible
    url(r'^admin/chronograph/job/(?P<pk>\d+)/run/$', 'chronograph.views.job_run', name='admin_chronograph_job_run'),
)

#urlpatterns += patterns('django.views.generic.simple',
#    url(r'^control/', 'direct_to_template', {'template': 'index.html'}),
#)
