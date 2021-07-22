from rest_framework import serializers


class BaseSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ('creation_time', 'modification_time')
