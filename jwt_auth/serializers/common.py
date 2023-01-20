from rest_framework import serializers
from django.contrib.auth import get_user_model, password_validation
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
  password = serializers.CharField(write_only=True)
  password_confirmation = serializers.CharField(write_only=True)

  def validate(self, data):
    password = data.pop('password')
    password_confirmation = data.pop('password_confirmation')

    if password != password_confirmation:
      raise ValidationError({'password_confirmation': 'Passwords do not match'})

    try:
      password_validation.validate_password(password=password)
    except ValidationError as err:
      raise ValidationError({'password': err.messages})

    data['password'] = make_password(password)

    return data

  # class Meta:
  #   model = User
  #   fields = ('id', 'email', 'username', 'first_name', 'last_name', 'profile_image', 'number_of_red_packets', 'items', 'multiplier')
  #   read_only_fields = ('is_active', 'is_staff', 'password', 'password_confirmation')
  #   # extra_kwargs = {
  #   #   'password': {'write_only': True},
  #   #   'password_confirmation': {'write_only': True}
  #   # }

  class Meta:
    model = User
    fields = ('id', 'email', 'username', 'first_name', 'last_name', 'profile_image', 'password', 'password_confirmation', 'number_of_red_packets', 'items', 'multiplier')

