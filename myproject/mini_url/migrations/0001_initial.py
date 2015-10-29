# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MiniUrl',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('url', models.URLField(verbose_name='URL à réduire', unique=True)),
                ('code', models.CharField(max_length=6, unique=True)),
                ('date', models.DateTimeField(verbose_name="Date d'enregistrement", auto_now_add=True)),
                ('pseudo', models.CharField(max_length=255, null=True, blank=True)),
                ('nb_acces', models.IntegerField(verbose_name="Nombre d'accès à l'Url", default=0)),
            ],
            options={
                'verbose_name': 'Mini URL',
                'verbose_name_plural': 'Minis URL',
            },
        ),
    ]
