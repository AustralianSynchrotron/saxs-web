from django.conf.urls.defaults import *
from django.views.generic.simple import redirect_to

# Required as the admin library is used
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^analysis/', include('saxs_app_analysis.urls')),
    (r'^$', redirect_to, {'url': 'about/'}),
)
