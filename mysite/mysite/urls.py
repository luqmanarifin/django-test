from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'polls.views.hello'),
    url(r'^lala/(?P<pk>[0-9]+)/$', 'polls.views.hello'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^coba/(?P<id>\d+)/$', 'polls.views.hello'),
    url(r'^coba/(?P<id>\d+)/likes', 'polls.views.likes'),
)
