

from django_countries.serializers import CountryFieldMixin
from rest_framework import serializers
from biocalc.models import Address

class AddressReadOnlySerializer(CountryFieldMixin, serializers.ModelSerializer):
    """
    Serializer class to seralize Address model
    """
    user = serializers.CharField(source='user.get_full_name', read_only=True)

    class Meta:
        model = Address
        fields = '__all__'

