# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activities',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('userName', models.CharField(max_length=100)),
                ('userFirstName', models.CharField(max_length=50)),
                ('userLastName', models.CharField(max_length=50)),
                ('userId', models.CharField(max_length=50, serialize=False, primary_key=True)),
                ('userLastOnline', models.DateTimeField(verbose_name=b'Last Online')),
                ('userActivities', models.CharField(max_length=100)),
                ('userEmail', models.EmailField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='activities',
            name='activitiesUserId',
            field=models.ForeignKey(to='meetup.User'),
        ),
    ]
