from taskconnect.models import *    # TODO: Change this later?
from rest_framework import serializers
from rest_framework_bulk import BulkListSerializer, BulkSerializerMixin

class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = ('name', 'description', 'editors', 'id', 'draft', 'clipboard', 'deleted', 'published')