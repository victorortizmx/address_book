# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contacts', '0003_auto_20150901_0129'),
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='contact',
            field=models.ManyToManyField(to='contacts.Contact', verbose_name=b'Contactos'),
        ),
        migrations.AddField(
            model_name='group',
            name='user',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='group',
            name='description',
            field=models.CharField(max_length=255, verbose_name=b'Descripcion'),
        ),
        migrations.AlterField(
            model_name='group',
            name='name',
            field=models.CharField(max_length=255, verbose_name=b'Nombre'),
        ),
    ]
