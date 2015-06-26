# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recommand', '0012_auto_20150623_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course_score',
            name='c_id',
            field=models.ForeignKey(to='recommand.course'),
        ),
        migrations.AlterField(
            model_name='raw_course',
            name='c_id',
            field=models.ForeignKey(to='recommand.course'),
        ),
        migrations.AlterField(
            model_name='user_course',
            name='c_id',
            field=models.ForeignKey(to='recommand.course'),
        ),
    ]
