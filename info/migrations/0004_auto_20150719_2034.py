# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0003_auto_20150719_0101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='path',
            field=sorl.thumbnail.fields.ImageField(upload_to='info/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='cover_image',
            field=models.ForeignKey(to='info.Image', null=True, blank=True),
        ),
    ]
