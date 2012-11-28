from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *
from django.views.generic import ListView
from control.models import Riego
from django.views.generic import TemplateView
from django.contrib import admin
import temperaturas.views
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^control/', include('control.urls')),
    url(r'', include('control.urls')),
    url(r'^temp/', include('temperaturas.urls')),
    url(r'^temp2/',  'temperaturas.views.results'),
    url(r'^mois/', include('moisture.urls')),
    url(r'^riegos/',ListView.as_view(
            queryset=Riego.objects.order_by('-pub_date'),
            context_object_name='latest_riego_list',
            template_name='riegos/index.html'),
            name='riegos_index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/chronograph/job/(?P<pk>\d+)/run/$', 'chronograph.views.job_run', name='admin_chronograph_job_run'),
)

