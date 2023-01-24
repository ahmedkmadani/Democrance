from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from app.models.customer import Customers
from app.serializers.customer import CustomerSerializer
from rest_framework import filters


class CustomerView(viewsets.ModelViewSet):
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["first_name", "last_name", "dob"]
    serializer_class = CustomerSerializer
    queryset = Customers.objects.all()

