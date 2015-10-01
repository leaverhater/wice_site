# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('date_created', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('path', models.CharField(max_length=255)),
                ('date_created', models.DateTimeField(verbose_name='date published')),
                ('gallery', models.ForeignKey(to='info.Gallery', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('short_description', models.CharField(max_length=255)),
                ('description', models.TextField(default='')),
                ('date_created', models.DateTimeField(verbose_name='date published')),
                ('cover_image', models.ForeignKey(to='info.Image')),
                ('gallery', models.ForeignKey(to='info.Gallery', null=True)),
            ],
        ),
    ]
