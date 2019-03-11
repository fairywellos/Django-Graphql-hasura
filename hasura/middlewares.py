import os

from django.contrib.contenttypes.models import ContentType
from django.db import connection
from django.http import JsonResponse
from rest_framework import status
from tenant_schemas.middleware import DefaultTenantMiddleware
from tenant_schemas.utils import get_tenant_model


class SAASMiddleware(DefaultTenantMiddleware):
    def process_request(self, request):
        super().process_request(request)
        webhook_url = os.getenv('HASURA_SAAS_AUTH_WEBHOOK', '/hasura/webhook/auth/')
        if webhook_url and webhook_url in request.build_absolute_uri():
            meta = request.META
            schema_from_header = meta.get('X-HASURA-TARGET-SCHEMA', meta.get('HTTP_X_HASURA_TARGET_SCHEMA', None))
            if not schema_from_header:
                return JsonResponse(data='You need to set header \'X-HASURA-TARGET-SCHEMA\' to the target sub-domain '
                                         'name', status=status.HTTP_401_UNAUTHORIZED, safe=False)
            tenant = get_tenant_model().objects.get(schema_name=schema_from_header)
            request.tenant = tenant
            connection.set_tenant(request.tenant)
            ContentType.objects.clear_cache()
