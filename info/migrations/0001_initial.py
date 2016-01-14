# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-13 14:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('date_created', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(verbose_name='date published')),
                ('path', sorl.thumbnail.fields.ImageField(upload_to='info/')),
                ('gallery', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='info.Gallery')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('short_description', models.CharField(max_length=255)),
                ('description', models.TextField(default='')),
                ('date_created', models.DateTimeField(verbose_name='date published')),
                ('cover_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='info.Image')),
                ('gallery', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='info.Gallery')),
            ],
        ),
    ]
