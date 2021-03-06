from django.conf.urls import patterns, include, url
from django.contrib import admin

from views import hello, page_404, current_datetime, hours_ahead, display_meta, search_form, search, contact, get_name
from beyond.views import index


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'robot.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url('^hello/$', hello),
    url("^408/$", page_404),
    url('^time/$', current_datetime),
    url(r'^time/plus/(\d{1,2})/$', hours_ahead),
    url(r'^meta/$', display_meta),
    url(r'^search-form/$', search_form),
    url(r'^search/$', search),
    url(r'^contact/$', contact),
    url(r'^name/$', get_name),
    url(r'^index/$', index),
)
