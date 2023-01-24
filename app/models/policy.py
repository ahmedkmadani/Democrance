from django.db import models
from app.models.customer import Customers
from app.models.quote import Quotes


class Policy(models.Model):
    NEW = 'new'
    QUOTED = 'quoted'
    ACTIVE = 'active'

    StatusChoices = [
        (NEW, 'new'),
        (QUOTED, 'quoted'),
        (ACTIVE, 'active'),
    ]

    customer = models.ForeignKey(Customers, on_delete=models.PROTECT)
    quote = models.ForeignKey(Quotes, on_delete=models.PROTECT)
    state = models.CharField(max_length=50, default=NEW, choices=StatusChoices)
    created_at = models.DateTimeField(auto_now_add=True)
