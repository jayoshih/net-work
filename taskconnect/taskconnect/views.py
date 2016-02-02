import json
from rest_framework import status
from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core import paginator
from django.core.files.storage import get_storage_class
from django.template import RequestContext
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from taskconnect.models import Channel
from taskconnect.serializers import ChannelSerializer


def base(request):
    return render(request, 'base.html')

@login_required
def challenge_list(request):
    channel_list = Channel.objects.all() # Todo: only allow access to certain channels?
    channel_serializer = ChannelSerializer(channel_list, many=True)
    return render(request, 'challenge_list.html', {"channels" : JSONRenderer().render(channel_serializer.data)})

@login_required
def task_list(request):
    channel_list = Channel.objects.all() # Todo: only allow access to certain channels?
    channel_serializer = ChannelSerializer(channel_list, many=True)
    return render(request, 'task_list.html', {"channels" : JSONRenderer().render(channel_serializer.data)})

@login_required
def friends_list(request):
    channel_list = Channel.objects.all() # Todo: only allow access to certain channels?
    channel_serializer = ChannelSerializer(channel_list, many=True)
    return render(request, 'friends_list.html', {"channels" : JSONRenderer().render(channel_serializer.data)})

@login_required
def settings(request):
    channel_list = Channel.objects.all() # Todo: only allow access to certain channels?
    channel_serializer = ChannelSerializer(channel_list, many=True)
    return render(request, 'settings.html', {"channels" : JSONRenderer().render(channel_serializer.data)})

@login_required
def achievements_list(request):
    channel_list = Channel.objects.all() # Todo: only allow access to certain channels?
    channel_serializer = ChannelSerializer(channel_list, many=True)
    return render(request, 'achievements_list.html', {"channels" : JSONRenderer().render(channel_serializer.data)})