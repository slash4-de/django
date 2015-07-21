from django.db import models

from django.contrib.auth.models import User

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
    duration = models.CharField(
        max_length=20,
        help_text='e.g. 3 hours, 5 days'
    )

    guest = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return "%s" % self.title
