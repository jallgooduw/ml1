# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('urlexpander', '0003_auto_20150808_1146'),
    ]

    operations = [
        migrations.AddField(
            model_name='urlexp',
            name='finaldestination',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='urlexp',
            name='httpstat',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='urlexp',
            name='pagetitle',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='urlexp',
            name='shorturl',
            field=models.URLField(null=True),
        ),
    ]
