from django.conf import settings
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from clients.models import Client
from users.api.serializers import UserSerializer
from users.models import UserProxy as User


class UserViewSet(ModelViewSet):
    permission_classes = (AllowAny,)

    def get_queryset(self):
        return User.objects.all()

    serializer_class = UserSerializer

    @action(methods=['GET'], detail=False, url_path='subdomain-by-host')
    def subdomain_by_host(self, request, **kwargs):
        """Carries URL param 'hostname' for a GET request"""
        hostname = self.request.query_params.get('hostname', '')
        domain = self.request.query_params.get('domain', '')
        match = hostname.replace(domain, settings.MAIN_DOMAIN_URL)
        subdomain = get_object_or_404(Client, domain_url=match)
        return Response({'domain_url': subdomain.domain_url, 'subdomain': subdomain.schema_name}, status=200)
