

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class API_Login_Serializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        print(cls, user)
        token = super().get_token(user)
        token['name'] = user.username
        token['editor'] = user.is_staff
        token['admin'] = user.is_superuser
        return token
    

from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField
from django.contrib.auth import authenticate
from django.utils.translation import gettext as _
from biocalc.exceptions import (
    InvalidCredentialsException,
    AccountDisabledException,
)

class UserLoginSerializer(serializers.Serializer):
    """
    Serializer to login users with email or phone number.
    """
    phone_number = PhoneNumberField(required=False, allow_blank=True)
    email = serializers.EmailField(required=False, allow_blank=True)
    password = serializers.CharField(
        write_only=True, style={'input_type': 'password'})

    def _validate_phone_email(self, phone_number, email, password):
        user = None

        if email and password:
            user = authenticate(username=email, password=password)
        elif str(phone_number) and password:
            user = authenticate(username=str(phone_number), password=password)
        else:
            raise serializers.ValidationError(
                _("Enter a phone number or an email and password."))

        return user

    def validate(self, validated_data):
        phone_number = validated_data.get('phone_number')
        email = validated_data.get('email')
        password = validated_data.get('password')

        user = None

        user = self._validate_phone_email(phone_number, email, password)

        if not user:
            raise InvalidCredentialsException()

        if not user.is_active:
            raise AccountDisabledException()

        if email:
            email_address = user.emailaddress_set.filter(
                email=user.email, verified=True).exists()
            if not email_address:
                raise serializers.ValidationError(_('E-mail is not verified.'))

        else:
            if not user.phone.is_verified:
                raise serializers.ValidationError(
                    _('Phone number is not verified.'))

        validated_data['user'] = user
        return validated_data
