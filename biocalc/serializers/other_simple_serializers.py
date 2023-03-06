
from rest_framework import serializers
from biocalc.models import (
    Fish,
    Plant,
    Tank,
    PlantCategory,
    FishCategory,
    SocialSegment,
    Comment,
    ItemGalleryImage,
    ItemSellingData,
    ) 

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"

class ItemGalleryImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemGalleryImage
        fields = "__all__"

class ItemSellingDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemSellingData
        fields = "__all__"


class SocialSegmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialSegment
        fields = "__all__"

class FishCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FishCategory
        fields = '__all__'

class FishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fish
        fields = '__all__'

class PlantCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantCategory
        fields = '__all__'

class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = '__all__'

class TankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tank
        fields = '__all__'

