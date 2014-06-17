from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'core.views.home', name='home'),
    url(r'^agencia/(?P<agency_name>[(\w|\d|%)-]+)/$', 'core.views.agency', name='agency')
)
