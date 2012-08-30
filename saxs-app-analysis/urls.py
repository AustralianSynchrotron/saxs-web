from django.conf.urls.defaults import *
from django.views.generic.simple import redirect_to

#to enable the admin site:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^media/?(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': '/usr/local/share/saxs/media/', 'show_indexes': True}),
    (r'^admin/', include(admin.site.urls)),
    (r'^analysis$', redirect_to, {'url': '/analysis/'}),
    (r'^analysis/?', include('saxs_app_analysis.urls')),
)

