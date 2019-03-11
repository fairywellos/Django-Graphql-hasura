from django.contrib import admin


# Register your models here.
from hasura.models import Permission


class PermissionAdmin(admin.ModelAdmin):
    fields = ('type', 'add_args', 'remove_args')


admin.site.register(Permission, PermissionAdmin)
