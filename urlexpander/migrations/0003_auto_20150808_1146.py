# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('urlexpander', '0002_auto_20150808_1043'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='urlexp',
            name='finaldestination',
        ),
        migrations.RemoveField(
            model_name='urlexp',
            name='httpstat',
        ),
        migrations.RemoveField(
            model_name='urlexp',
            name='pagetitle',
        ),
    ]
