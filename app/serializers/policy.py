from rest_framework import serializers
from app.models.policy import Policy
from app.models.customer import Customers
from app.models.quote import Quotes
from app.serializers.customer import CustomerSerializer


class PolicySerializer(serializers.ModelSerializer):
    # TODO: return customer full name instead of pk + return Quote details
    class Meta:
        model = Policy
        fields = ("customer", "quote", "state", "created_at")
