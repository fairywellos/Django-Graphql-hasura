import random
import string

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    USERNAME_FIELD = 'email'
    email = models.EmailField(_('email address'), unique=True)
    is_tenant = models.BooleanField(default=False, help_text='When this is true at creation time, this user becomes a '
                                                             'tenant under the main')
    REQUIRED_FIELDS = []


def create_tenant(sender, instance, **kwargs):
    if kwargs.get('created') and instance.is_tenant:
        from clients.models import Tenant

        def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
            return ''.join(random.choice(chars) for _ in range(size))

        tenant_sub_domain = instance.username or instance.first_name or instance.last_name or id_generator()
        Tenant.objects.create(name=instance.first_name, domain_url=f'{tenant_sub_domain}.{settings.MAIN_DOMAIN_URL}',
                              paid_until=None, on_trial=True)


post_save.connect(create_tenant, User)


class UserProxy(User):
    """Create methods and functions over the user model here"""

    class Meta:
        proxy = True
