
from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework import serializers
from biocalc.exceptions import AccountNotRegisteredException
from django.contrib.auth.models import User
from biocalc.models import PhoneNumber

class PhoneNumberSerializer(serializers.ModelSerializer):
    """
    Serializer class to serialize phone number.
    """
    phone_number = PhoneNumberField()

    class Meta:
        model = PhoneNumber
        fields = ('phone_number',)

    def validate_phone_number(self, value):
        try:
            queryset = User.objects.get(phone__phone_number=value)
            if queryset.phone.is_verified == True:
                err_message = _('Phone number is already verified')
                raise serializers.ValidationError(err_message)

        except User.DoesNotExist:
            raise AccountNotRegisteredException()

        return value

