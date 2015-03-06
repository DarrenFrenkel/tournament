# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tournament',
            options={'get_latest_by': 'created'},
        ),
        migrations.AddField(
            model_name='tournament',
            name='players',
            field=models.ManyToManyField(to='matches.Player', null=True, blank=True),
            preserve_default=True,
        ),
    ]
