from django.db import models
from tenant_schemas.models import TenantMixin


class Client(TenantMixin):
    name = models.CharField(max_length=100)
    paid_until = models.DateField(null=True, blank=True)
    on_trial = models.BooleanField(default=True)
    created_on = models.DateField(auto_now_add=True)

    # default true, schema will be automatically created and synced when it is saved
    auto_create_schema = True


class TenantManager(models.Manager):
    def get_queryset(self):
        return super(TenantManager, self).get_queryset().exclude(schema_name='public')


class Tenant(Client):
    objects = TenantManager()

    class Meta:
        proxy = True
