from rest_framework import serializers

from shop.models import TsunList
from shop.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'password')

class TsunListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TsunList
        fields = ('id', 'UserId', 'title','category','tsuntype','link','memo','exp','read','created_at')

