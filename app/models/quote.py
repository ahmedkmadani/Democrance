from django.db import models


class Quotes(models.Model):

    NEW = 'New'
    QUOTED = 'Quoted'
    ACTIVE = 'Active'

    StatusChoices = [
        (NEW, 'New'),
        (QUOTED, 'Quoted'),
        (ACTIVE, 'Active'),
    ]

    type = models.CharField(max_length=255)
    premium = models.IntegerField(null=False)
    cover = models.IntegerField(null=False)
    state = models.CharField(max_length=50, default=NEW, choices=StatusChoices)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.type

