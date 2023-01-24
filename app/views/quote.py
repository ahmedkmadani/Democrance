

from rest_framework import viewsets

from app.models.quote import Quotes
from app.serializers.quote import QuotesSerializer


class QuotesView(viewsets.ModelViewSet):
    serializer_class = QuotesSerializer
    queryset = Quotes.objects.all()

