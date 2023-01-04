from rest_framework import serializers
from app.models.customer import Customers

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = ("pk", "first_name", "last_name", "dob")
