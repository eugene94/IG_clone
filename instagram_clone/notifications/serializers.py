from rest_framework import serializers
from . import models
from instagram_clone.images import serializers as image_serializers
from instagram_clone.users import serializers as user_serializers


class NotificationSerializer(serializers.ModelSerializer):

    creator = user_serializers.ListUserSerializer()
    image = image_serializers.SmallImageSerializer()

    class Meta:
        model = models.Notification
        fields = "__all__"
