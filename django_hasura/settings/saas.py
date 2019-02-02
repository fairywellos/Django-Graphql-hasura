SHARED_APPS = [
    'tenant_schemas',
    'clients',
]  # Just to make sure I remember what I'm doing in the next 2hrs, lol. These apps are synced to the public schema ONLY

TENANT_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'users',
]  # These ones are synced to the individual schemas (ALL), it will be applied to public anyways

DATABASE_ROUTERS = (
    'tenant_schemas.routers.TenantSyncRouter',
)

TENANT_MODEL = "clients.Client"

DEFAULT_FILE_STORAGE = 'tenant_schemas.storage.TenantFileSystemStorage'

# PG_EXTRA_SEARCH_PATHS = ['extensions']

TENANT_LIMIT_SET_CALLS = True
PUBLIC_SCHEMA_URLCONF = 'django_hasura.urls_public'
