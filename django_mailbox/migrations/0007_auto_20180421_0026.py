# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2018-04-21 00:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_mailbox', '0008_message_uid'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mailbox',
            options={'verbose_name': 'Mailbox', 'verbose_name_plural': 'Mailboxes'},
        ),
        migrations.AlterModelOptions(
            name='message',
            options={'verbose_name': 'E-mail message', 'verbose_name_plural': 'E-mail messages'},
        ),
        migrations.AlterModelOptions(
            name='messageattachment',
            options={'verbose_name': 'Message attachment', 'verbose_name_plural': 'Message attachments'},
        ),
    ]
