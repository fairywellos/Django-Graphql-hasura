from django.contrib.postgres.fields import JSONField
from django.db import models
from django.utils.translation import ugettext_lazy as _

PERMISSIONS = (
    (_('insert_permission'), 'Permission to insert to graphql'),
    (_('select_permission'), 'Permission to select from graphql'),
    (_('update_permission'), 'Permission to update record graphql'),
    (_('delete_permission'), 'Permission to delete from graphql'),
)


class Permission(models.Model):
    type = models.CharField(max_length=30, choices=PERMISSIONS)
    add_args = JSONField(help_text='Args to create permission')
    remove_args = JSONField(help_text='Args to call when deleting permission')

    def __str__(self):
        return self.type
