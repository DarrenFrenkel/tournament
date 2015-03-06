# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0006_auto_20150305_0154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='player_two',
            field=models.ForeignKey(related_name='player_two', to='matches.Player'),
            preserve_default=True,
        ),
    ]
