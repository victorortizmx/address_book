# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contacts', '0002_auto_20150827_0237'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='person',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='phone_number',
        ),
        migrations.AddField(
            model_name='contact',
            name='number',
            field=models.IntegerField(default=55555555, verbose_name=b'Numero'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='user',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contact',
            name='address',
            field=models.CharField(max_length=255, null=True, verbose_name=b'Direccion', blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=254, null=True, verbose_name=b'Correo', blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='last_name',
            field=models.CharField(max_length=255, null=True, verbose_name=b'Apellidos', blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=255, verbose_name=b'Nombre'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='type_number',
            field=models.IntegerField(verbose_name=b'Tipo', choices=[(1, b'Movil'), (2, b'Casa'), (3, b'Oficina')]),
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]
