from rest_framework import serializers
from app.models.quote import Quotes


class QuotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quotes
        fields = '__all__'
