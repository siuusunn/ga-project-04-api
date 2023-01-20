from .common import PocketSerializer
from jwt_auth.serializers.common import UserSerializer

class PopulatedPocketSerializer(PocketSerializer):
  owner = UserSerializer()