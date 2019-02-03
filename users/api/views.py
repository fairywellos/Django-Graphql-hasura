from rest_framework.viewsets import ModelViewSet

from users.api.serializers import UserSerializer
from users.models import UserProxy as User


class UserViewSet(ModelViewSet):
    def get_queryset(self):
        return User.objects.all()

    serializer_class = UserSerializer
