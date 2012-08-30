from django.conf.urls.defaults import *

urlpatterns = patterns('saxs_app_analysis.views',
    (r'^(?P<type>.+)/(?P<epn>.+)/(?P<experiment>.+)/json/?$', 'get_feed', {'feed': 'json'}),
    (r'^plot_profile/(?P<profile>.+)/?$', 'get_profile_png'),
    (r'^(?P<type>.+)/(?P<epn>\d+)/?$', 'main'),
    (r'^(?P<type>.+)/?$', 'main'),
)
