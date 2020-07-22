from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):    
    class Meta:
        model = User
        fields = ('id', 'name', 'status', 'country', 'town', 'subscriptionsStatus', 'ava')

class ProfileSerializer(serializers.ModelSerializer):    
    class Meta:
        model = User
        fields = ('id', 'name', 'status', 'friendsCount', 'subscribersCount', 'photosCount', 'audiosCount')