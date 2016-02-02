"""URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.conf import settings
from django.contrib import admin
from django.contrib.auth import views as auth_views
from rest_framework import routers, viewsets
from rest_framework.permissions import AllowAny
from taskconnect.models import *
import serializers
import views

class ChannelViewSet(viewsets.ModelViewSet):
    queryset = Channel.objects.all()
    serializer_class = serializers.ChannelSerializer


router = routers.DefaultRouter()
router.register(r'channel', ChannelViewSet)

urlpatterns = [
    url(r'^$', views.base, name='base'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^accounts/logout/$', auth_views.logout, {'template_name': 'registration/logout.html'}),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^challenges/$', views.challenge_list, name='challenges'),
    url(r'^friends/$', views.friends_list, name='friends'),
    url(r'^settings/$', views.settings, name='settings'),
    url(r'^achievements/$', views.achievements_list, name='achievements'),
    url(r'^todo/$', views.task_list, name='tasks'),
    #url(r'channels/(?P<channel_id>\w+)', views.channel, name='channel'),
]


urlpatterns += [url(r'^jsreverse/$', 'django_js_reverse.views.urls_js', name='js_reverse')]

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT})]
