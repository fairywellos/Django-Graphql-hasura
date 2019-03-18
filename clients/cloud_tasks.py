import random
import string

from django.conf import settings
from django_cloud_tasks import task

from users.models import User


@task(queue='default')
def create_tenant_task(request, user_id):
    user = User.objects.get(pk=user_id)
    from clients.models import Client

    def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))

    tenant_sub_domain = user.username or user.first_name or user.last_name or id_generator()
    tenant = Client(name=user.get_full_name(), user=user,
                    domain_url=f'{tenant_sub_domain}.{settings.MAIN_DOMAIN_URL}',
                    paid_until=None, on_trial=True, schema_name=tenant_sub_domain)
    tenant.save()
