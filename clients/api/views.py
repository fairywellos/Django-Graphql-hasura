from rest_framework.viewsets import ModelViewSet

from clients.api.serializers import TenantSerializer
from clients.models import Tenant


class ClientsViewSet(ModelViewSet):
    def get_queryset(self):
        return Tenant.objects.all().order_by('-created_on')

    serializer_class = TenantSerializer
