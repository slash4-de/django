from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(default='')
    venue = models.CharField(max_length=100)
    seats = models.IntegerField()
    amount = models.DecimalField(
        max_digits=11,
        decimal_places=2
    )
    date = models.DateTimeField()
