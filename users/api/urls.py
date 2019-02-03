from rest_framework.routers import DefaultRouter
from users.api import views

router = DefaultRouter()
router.register('', views.UserViewSet, base_name='users')

urlpatterns = router.urls
