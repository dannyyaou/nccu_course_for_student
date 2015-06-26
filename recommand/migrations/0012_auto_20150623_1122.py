# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recommand', '0011_raw_course_rc_department'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_detail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('u_id', models.IntegerField()),
                ('u_name', models.CharField(default=b'', max_length=10)),
                ('u_studentid', models.CharField(default=b'', max_length=10)),
                ('u_depart', models.CharField(default=b'', max_length=20)),
                ('u_grade', models.CharField(default=b'', max_length=5)),
            ],
        ),
        migrations.DeleteModel(
            name='user',
        ),
    ]
