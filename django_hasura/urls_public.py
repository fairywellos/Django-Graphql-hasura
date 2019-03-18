from django.contrib import admin
from django.urls import path, include
from django_cloud_tasks import urls as dct_urls

from django_hasura.settings import IS_GAE

api_patterns = [
    path('clients/', include('clients.api.urls')),
    path('users/', include('users.api.urls')),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hasura/', include('hasura.urls')),
    path('api/v1/', include(api_patterns)),
]

if IS_GAE:
    urlpatterns += [path('_tasks/', include(dct_urls))]
