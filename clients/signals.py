from django.apps import apps
from django.conf import settings
from tenant_schemas.models import TenantMixin
from tenant_schemas.signals import post_schema_sync
from tenant_schemas.utils import tenant_context

from hasura.api.schema.tables import track


def hasura_auto_track_tables(sender, tenant, **kwargs):
    apps_to_track_tables = settings.TENANT_APPS
    for app in apps_to_track_tables:
        models = apps.all_models[app]
        for key in models.keys():
            Model = models[key]
            if hasattr(Model, 'Hasura') and Model.Hasura.track:
                track(tenant.schema_name, Model._meta.db_table)
    # Replicates the user login to their schema
    user = tenant.user
    with tenant_context(tenant):
        user.id = None
        user.is_tenant = False
        user.is_staff = True
        user.is_superuser = True
        user.save()


post_schema_sync.connect(hasura_auto_track_tables, sender=TenantMixin)
