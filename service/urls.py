from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import url

from service import views

urlpatterns = [
    url(r'^parkings/$', views.ParkingList.as_view()),
    url(r'^parkings/(?P<pk>[0-9]+)/$', views.ParkingDetail.as_view()),
]


urlpatterns = format_suffix_patterns(urlpatterns)
