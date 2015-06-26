# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recommand', '0013_auto_20150623_1149'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_detail',
            name='u_fid',
            field=models.CharField(default=b'', max_length=50),
        ),
    ]
