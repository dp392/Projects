from django.conf.urls import url, patterns
from . import views

urlpatterns = patterns('',
    url(r'^$', views.home),
    url(r'^matches/([0-9]{1,20})/$', views.matches),
    url(r'^user/', views.user),
    url(r'^addActivities/', views.addActivities),
)