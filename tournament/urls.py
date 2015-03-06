from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'matches.views.home', name='home'),
    url(r'^winner/(?P<match_id>\d+)$', 'matches.views.winner', name='winner'),
    url(r'^new_tournament/$', 'matches.views.new_tournament', name='new_tournament')
)
