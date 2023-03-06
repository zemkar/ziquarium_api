
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField


class AquaProfile(models.Model):
    """
    Related model of user profile.

    contain:\n
        :key user -       Related field, owner.
        :key bio -        Text field (max_length=500), something about.
        :key location -   Char field (max_length=30), place.
        :key birth_date - Date field, birth date.
    """
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.user} profile"


class PhoneNumber(models.Model):
    user = models.OneToOneField(
        User, related_name='phone', on_delete=models.CASCADE)
    phone_number = PhoneNumberField(unique=True)
    is_verified = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at', )

    def __str__(self):
        return self.phone_number.as_e164


class Address(models.Model):

    ADDRESS_CHOICES = (("B","BILLING"), ("S","SHIPPING"))

    user = models.ForeignKey(
        User, related_name='addresses', on_delete=models.CASCADE)
    address_type = models.CharField(max_length=1, choices=ADDRESS_CHOICES)
    default = models.BooleanField(default=False)
    country = CountryField()
    city = models.CharField(max_length=100)
    street_address = models.CharField(max_length=100)
    apartment_address = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at', )

    def __str__(self):
        if self.address_type == "B":
            return f"BILLING of {self.user.get_full_name()}"
        if self.address_type == "S":
            return f"SHIPPING of {self.user.get_full_name()}"
        return "error address"