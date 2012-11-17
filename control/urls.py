from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
 

urlpatterns = patterns('',
    url(r'^$',TemplateView.as_view(template_name="control/centrocontrol.html"),
        name='control_index'),
    url(r'^releOn', 'control.views.releOn'),
    url(r'^humedad', 'control.views.humedad'),
    url(r'^temperatura', 'control.views.temperatura'),

)
