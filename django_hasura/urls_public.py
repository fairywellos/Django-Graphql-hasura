from django.contrib import admin
from django.urls import path, include
from django_cloud_tasks import urls as dct_urls

from clients.views import HomePageView

api_patterns = [
    path('clients/', include('clients.api.urls')),
    path('users/', include('users.api.urls')),
]

urlpatterns = [
    path('', HomePageView.as_view()),
    path('admin/', admin.site.urls),
    path('hasura/', include('hasura.urls')),
    path('api/v1/', include(api_patterns)),
]

urlpatterns += [path('_tasks/', include(dct_urls))]
