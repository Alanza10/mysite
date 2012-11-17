from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView
from temperaturas.models import Temperatura

urlpatterns = patterns('',
    url(r'^$',
        ListView.as_view(
            queryset=Temperatura.objects.order_by('-pub_date')[:10],
            context_object_name='latest_temp_list',
            template_name='temp/index.html'),
        name='temp_index'),

)
