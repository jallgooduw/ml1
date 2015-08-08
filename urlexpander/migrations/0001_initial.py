# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='URL',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('shorturl', models.URLField()),
                ('httpstat', models.PositiveIntegerField()),
                ('finaldestination', models.URLField()),
                ('pagetitle', models.TextField()),
            ],
        ),
    ]
