
from rest_framework import serializers
from django.contrib.auth.models import User
from biocalc.models import AquaProfile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'is_staff', 'is_superuser', 'last_login'] #"__all__"

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = AquaProfile
        fields = ['bio', 'location', 'birth_date'] #"__all__"
