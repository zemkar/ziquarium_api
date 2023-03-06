
from django.conf import settings
from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField
from biocalc.exceptions import AccountNotRegisteredException
from django.contrib.auth.models import User
from biocalc.models import PhoneNumber

class VerifyPhoneNumberSerialzier(serializers.Serializer):
    """
    Serializer class to verify OTP.
    """
    phone_number = PhoneNumberField()
    # otp = serializers.CharField(max_length=settings.TOKEN_LENGTH)

    def validate_phone_number(self, value):
        queryset = User.objects.filter(phone__phone_number=value)
        if not queryset.exists():
            raise AccountNotRegisteredException()
        return value

    def validate(self, validated_data):
        phone_number = str(validated_data.get('phone_number'))
        # otp = validated_data.get('otp')

        queryset = PhoneNumber.objects.get(phone_number=phone_number)

        # queryset.check_verification(security_code=otp)

        return validated_data

