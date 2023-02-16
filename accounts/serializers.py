from .models import User, Pirg
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    sponsor = serializers.StringRelatedField()
    class Meta:
        model = User
        fields = ["id", "firstname", "lastname", "username", "email", "is_pi", "sponsor"]


class PirgSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    owner = serializers.StringRelatedField()
    users = serializers.StringRelatedField(many=True)
    admins = serializers.StringRelatedField(many=True)
    class Meta:
        model = Pirg
        fields = ["id", "name", "owner", "users", "admins"]
