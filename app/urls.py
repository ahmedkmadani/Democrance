from django.urls import path, include
from rest_framework import routers
from app.views.customer import CustomerView
from app.views.quote import QuotesView
from app.views.policy import PolicyView
from app.views.pay import PayView


router = routers.DefaultRouter()
router.register(r"create_customer", CustomerView, basename="customer")
router.register(r"quote", QuotesView, basename="quote")
router.register(r"policy", PolicyView, basename="policy")


urlpatterns = [
    path("", include(router.urls)),
]
