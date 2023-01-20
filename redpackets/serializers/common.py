from rest_framework import serializers
from ..models import RedPackets

class RedPacketSerializer(serializers.ModelSerializer):
  class Meta:
    model = RedPackets
    fields = '__all__'