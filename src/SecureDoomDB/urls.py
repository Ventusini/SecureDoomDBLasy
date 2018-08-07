# api/urls.py

from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import IncidentsView
from .views import CarsView

urlpatterns = {
    url(r'^getIncidents/$', IncidentsView.as_view(), name="create"),
    url(r'^getCarsFlow/$', CarsView.as_view(), name="create"), 
}

urlpatterns = format_suffix_patterns(urlpatterns)