from rest_framework import serializers
from biocalc.models import Address
from django_countries.serializers import CountryFieldMixin


class ShippingAddressSerializer(CountryFieldMixin, serializers.ModelSerializer):
    """
    Serializer class to seralize address of type shipping
    For shipping address, automatically set address type to shipping
    """
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Address
        fields = '__all__'
        read_only_fields = ('address_type', )

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['address_type'] = 'S'

        return representation
