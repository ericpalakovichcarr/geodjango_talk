from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^ponypeople/', include('weloveponies.ponypeople.urls', namespace="ponypeople")),
    url(r'^admin/', include(admin.site.urls)),
)
