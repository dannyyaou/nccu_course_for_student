# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('recommand', '0009_auto_20150623_0533'),
    ]

    operations = [
        migrations.AddField(
            model_name='course_score',
            name='cs_createon',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 23, 5, 43, 29, 894249, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
