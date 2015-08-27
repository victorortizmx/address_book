# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0001_initial'),
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='contact',
            name='groups',
            field=models.ManyToManyField(to='groups.Group'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='type_number',
            field=models.PositiveIntegerField(choices=[(1, b'Movil'), (2, b'Casa'), (3, b'Oficina')]),
        ),
        migrations.AddField(
            model_name='contact',
            name='person',
            field=models.ForeignKey(to='contacts.Person', null=True),
        ),
    ]
