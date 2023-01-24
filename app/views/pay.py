
from rest_framework import viewsets
from rest_framework.views import APIView

from app.models.customer import Customers
from app.serializers.customer import CustomerSerializer


class PayView(viewsets.ViewSet):
    # TODO: when user hit this endpoint will pass Policy pk and update state to active
    def create(self, request, *args, **kwargs):
        pass
