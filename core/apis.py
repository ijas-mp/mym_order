from rest_framework import routers
from core import views as core_views

router = routers.DefaultRouter()

router.register("Item", core_views.ItemViewSet, basename="Item")
router.register("order", core_views.OrderViewSet, basename="order")
router.register("Address", core_views.AddressViewSet, basename="address")
