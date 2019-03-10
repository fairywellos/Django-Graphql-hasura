from django.contrib import admin
from django.urls import path, include


api_patterns = [
    path('clients/', include('clients.api.urls')),
    path('users/', include('users.api.urls')),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hasura/', include('hasura.urls')),
    path('api/v1/', include(api_patterns))
]
