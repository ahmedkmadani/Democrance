from django.contrib import admin
from app.models.customer import Customers
from app.models.quote import Quotes
from app.models.policy import Policy

# Register your models here.

admin.site.register(Customers)
admin.site.register(Quotes)
admin.site.register(Policy)
