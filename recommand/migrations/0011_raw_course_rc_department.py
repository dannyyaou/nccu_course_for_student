# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recommand', '0010_course_score_cs_createon'),
    ]

    operations = [
        migrations.AddField(
            model_name='raw_course',
            name='rc_department',
            field=models.CharField(default=b'', max_length=20),
        ),
    ]
