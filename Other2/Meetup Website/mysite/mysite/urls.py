from django.conf.urls import url, patterns, include
from django.contrib import admin

urlpatterns = [
    url(r'^', include('meetup.urls')),
    url(r'^matches/', include('meetup.urls')),
    url(r'^admin/', include(admin.site.urls)),
]