from .common import PocketSerializer
from jwt_auth.serializers.common import UserSerializer
from items.serializers.common import ItemSerializer

class PopulatedPocketSerializer(PocketSerializer):
  owner = UserSerializer()
  items = ItemSerializer(many=True)