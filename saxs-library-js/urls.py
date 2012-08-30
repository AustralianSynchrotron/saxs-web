from django.conf.urls.defaults import *
from django.views.generic.simple import redirect_to

urlpatterns = patterns('',
    (r'^media/?(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': '/usr/local/share/saxs/media/', 'show_indexes': True}),
    (r'^js/?', include('saxs_library_js.urls')),
)
