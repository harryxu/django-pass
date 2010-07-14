from django.conf.urls.defaults import *

from django_pass import views as pass_views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', pass_views.index, name='pass_index'),
    url(r'^passwordchange/$', pass_views.password_change, name='password_change'),
)
