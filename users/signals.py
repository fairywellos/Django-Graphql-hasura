import random
import string

import requests
from django.conf import settings
from django.db.models.signals import post_save
from tenant_schemas.models import TenantMixin
from tenant_schemas.signals import post_schema_sync

from users.models import UserProxy


def create_tenant(sender, instance, **kwargs):
    if kwargs.get('created') and instance.is_tenant:
        from clients.models import Client

        def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
            return ''.join(random.choice(chars) for _ in range(size))

        tenant_sub_domain = instance.username or instance.first_name or instance.last_name or id_generator()
        tenant = Client(name=instance.get_full_name(), user=instance,
                        domain_url=f'{tenant_sub_domain}.{settings.MAIN_DOMAIN_URL}',
                        paid_until=None, on_trial=True, schema_name=tenant_sub_domain)
        tenant.save()


def hasura_auto_track_table(sender, instance, **kwargs):
    response = requests.post(f'{settings.HASURA_URL}/v1/query')

post_save.connect(create_tenant, UserProxy)
post_schema_sync.connect(hasura_auto_track_table, TenantMixin)
