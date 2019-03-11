import random
import string

from django.conf import settings
from django.db.models.signals import post_save, pre_delete

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


def delete_tenant(sender, instance, **kwargs):
    if instance.is_tenant:
        from clients.models import Client
        Client.objects.filter(user=instance).delete()


post_save.connect(create_tenant, UserProxy)
pre_delete.connect(delete_tenant, UserProxy)
# We are using a pre delete signal and not letting it cascade because we need the schema also deleted
