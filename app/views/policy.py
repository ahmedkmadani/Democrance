from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from app.models.policy import Policy
from app.serializers.policy import PolicySerializer


class PolicyView(viewsets.ModelViewSet):
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["quote"]
    serializer_class = PolicySerializer
    queryset = Policy.objects.all()

