from .common import RedPacketSerializer
from jwt_auth.serializers.common import UserSerializer

class PopulatedRedPacketSerializer(RedPacketSerializer):
  owner = UserSerializer()