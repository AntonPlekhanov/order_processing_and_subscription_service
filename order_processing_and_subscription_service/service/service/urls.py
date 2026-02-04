from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from subscriptions.views import TariffView, UserSubscriptionView
from products.views import OrderView


router = routers.DefaultRouter()
router.register(r'api/tariffs', TariffView)
router.register(r'api/usersubscriptions', UserSubscriptionView)

router.register(r'api/orders', OrderView)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]



