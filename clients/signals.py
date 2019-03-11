from django.apps import apps
from django.conf import settings
from tenant_schemas.models import TenantMixin
from tenant_schemas.signals import post_schema_sync

from hasura.api.schema.tables import track


def hasura_auto_track_tables(sender, tenant, **kwargs):
    apps_to_track_tables = settings.HASURA_AUTO_TRACK_APPS
    for app in apps_to_track_tables:
        models = apps.all_models[app]
        for key in models.keys():
            Model = models[key]
            track(tenant.schema_name, Model._meta.db_table)


post_schema_sync.connect(hasura_auto_track_tables, sender=TenantMixin)
