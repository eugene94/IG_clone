from rest_framework.views import APIView
from rest_framework.response import Response
from . import models, serializers
from rest_framework import status


class Notification(APIView):

    def get(self, request, format=None):

        user = request.user

        notifications = models.Notification.objects.filter(creator=user)

        serializer = serializers.NotificationSerializer(notifications, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)


def create_notification(creator, to, type, image=None, comment=None):

    notification = models.Notification.objects.create(
        creator=creator,
        to=to,
        noti_type=type,
        image=image,
        comment=comment
    )
