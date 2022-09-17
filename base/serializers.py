from rest_framework.serializers import ModelSerializer
from .models import Profile


class ProfileImageUpdateSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = ['self_image']