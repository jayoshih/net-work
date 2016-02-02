# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(verbose_name='channel name', max_length=100)),
                ('description', models.TextField(verbose_name='channel description', help_text='Description of what a channel contains', max_length=300)),
                ('author', models.CharField(verbose_name='channel author', help_text='Channel author can be a person or an organization', max_length=100)),
                ('editors', models.ManyToManyField(verbose_name='editors', help_text='Users with edit rights', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Channel',
                'verbose_name_plural': 'Channels',
            },
        ),
    ]
