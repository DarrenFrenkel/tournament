# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0007_auto_20150305_0202'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tournament',
            old_name='name',
            new_name='tournament_name',
        ),
    ]
