# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='duration',
            field=models.CharField(help_text='e.g. 3 hours, 5 days', max_length=20, default=0),
            preserve_default=False,
        ),
    ]
