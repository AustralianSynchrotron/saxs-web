from django.conf.urls.defaults import *
from django.views.generic.simple import redirect_to

urlpatterns = patterns('saxs_library_js.views',
    (r'^(?P<type>.+)/?', 'test'),
)
