import base64

from rest_framework import serializers
from . import models

class BinaryBase64Field(serializers.Field):
    def to_representation(self, content):
        return base64.b64encode(content).decode('ascii')

    def to_internal_value(self, data):
        return base64.b64decode(data)

class EntrySerializer(serializers.ModelSerializer):
    content = BinaryBase64Field()

    class Meta:
        model = models.Entry
        fields = ('uuid', 'content')
