from django.urls import include, path
from rest_framework import routers
from movements.views import MovementViewSet

router = routers.DefaultRouter()
router.register(r"movements", MovementViewSet)

urlpatterns = [path("", include(router.urls))]
