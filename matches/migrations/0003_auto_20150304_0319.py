# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0002_auto_20150129_0557'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='tournament',
            field=models.ForeignKey(blank=True, to='matches.Tournament', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='match',
            name='winner',
            field=models.ForeignKey(related_name='winner', blank=True, to='matches.Player', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='tournament',
            name='max_players',
            field=models.PositiveIntegerField(default=4, choices=[(4, b'Four'), (8, b'Eight'), (16, b'Sixteen')]),
            preserve_default=True,
        ),
    ]
