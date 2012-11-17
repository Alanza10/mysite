from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView
from moisture.models import Moisture

urlpatterns = patterns('',
    url(r'^$',
        ListView.as_view(
            queryset=Moisture.objects.order_by('-pub_date')[:10],
            context_object_name='latest_mois_list',
            template_name='mois/index.html'),
        name='mois_index'),

)
