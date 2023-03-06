
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from phonenumber_field.serializerfields import PhoneNumberField
from biocalc.models import PhoneNumber
from django.utils.translation import gettext as _

class UserRegistrationSerializer(serializers.ModelSerializer):
    """
    Create User and store it into DB

    * 'username', 'password', 'password2', 'email' - required fields
    * 'first_name', 'last_name' - not required fields
    """
    
    first_name = serializers.CharField(required=False, write_only=True)
    last_name = serializers.CharField(required=False, write_only=True)
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    
    phone_number = PhoneNumberField(
        required=False,
        write_only=True,
        validators=[
            UniqueValidator(
                queryset=PhoneNumber.objects.all(),
                message=_(
                    "A user is already registered with this phone number."),
            )
        ],
    )

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name', 'phone_number')
        
    
    def validate(self, validated_data):
        email = validated_data.get('email', None)

        if not email:
            raise serializers.ValidationError(
                _("Enter an email."))

        if validated_data['password'] != validated_data['password2']:
            raise serializers.ValidationError(
                {"password": _("The two password fields didn't match.")})

        validated_data.pop("password2")
        return validated_data

    def create(self, validated_data):
        user = User.objects.create(
            username  =validated_data['username'],
            email = validated_data['email'],
            first_name = validated_data.get('first_name', ""),
            last_name = validated_data.get('last_name', "")
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def get_cleaned_data_extra(self):
        return {
            'phone_number': self.validated_data.get('phone_number', ''),
            "first_name": self.validated_data.get("first_name", ""),
            "last_name": self.validated_data.get("last_name", ""),
        }

    def create_extra(self, user, validated_data):
        user.first_name = self.validated_data.get("first_name")
        user.last_name = self.validated_data.get("last_name")
        user.save()

        phone_number = validated_data.get("phone_number")

        if phone_number:
            PhoneNumber.objects.create(user=user, phone_number=phone_number)
            user.phone.save()

    def custom_signup(self, request, user):
        self.create_extra(user, self.get_cleaned_data_extra())
