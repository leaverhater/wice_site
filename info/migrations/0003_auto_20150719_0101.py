# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0002_auto_20150718_2114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='path',
            field=models.ImageField(upload_to='info/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='cover_image',
            field=models.ForeignKey(to='info.Image', null=True),
        ),
    ]
