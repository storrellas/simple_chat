# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_auto_20151109_0746'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message', models.CharField(default=b'', max_length=250)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('chat_user', models.ForeignKey(to='chat.ChatUser')),
            ],
        ),
    ]
