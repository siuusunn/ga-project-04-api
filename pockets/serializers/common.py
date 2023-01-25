from rest_framework import serializers
from ..models import Pocket

class PocketSerializer(serializers.ModelSerializer):
  class Meta:
    model = Pocket
    fields = '__all__'