# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wetravel', '0002_userprofile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(default=b'static/images/default_image.png', upload_to=b'images/', null=True, verbose_name=b'Profile Pic', blank=True),
            preserve_default=True,
        ),
    ]
