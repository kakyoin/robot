from django.conf.urls import patterns, include, url
from django.contrib import admin

from views import hello, page_404, current_datetime, hours_ahead


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'robot.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url('^hello/$', hello),
    url("^406/$", page_404),
    url('^time/$', current_datetime),
    url(r'^time/plus/(\d{1,2})/$', hours_ahead),
)
