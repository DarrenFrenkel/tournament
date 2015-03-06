# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0003_auto_20150304_0319'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Game',
        ),
        migrations.AlterModelOptions(
            name='match',
            options={'verbose_name_plural': 'matches'},
        ),
        migrations.AlterField(
            model_name='match',
            name='tournament',
            field=models.ForeignKey(to='matches.Tournament'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tournament',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
            preserve_default=True,
        ),
    ]
