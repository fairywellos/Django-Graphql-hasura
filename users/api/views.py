from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from users.api.serializers import UserSerializer
from users.models import UserProxy as User


class UserViewSet(ModelViewSet):
    permission_classes = (AllowAny,)

    def get_queryset(self):
        return User.objects.all()

    serializer_class = UserSerializer
