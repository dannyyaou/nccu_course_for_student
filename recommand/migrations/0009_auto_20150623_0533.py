# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recommand', '0008_auto_20150620_0603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course_score',
            name='c_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='course_score',
            name='u_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='raw_course',
            name='c_id',
            field=models.IntegerField(default=b''),
        ),
        migrations.AlterField(
            model_name='user_course',
            name='c_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='user_course',
            name='u_id',
            field=models.IntegerField(),
        ),
    ]
