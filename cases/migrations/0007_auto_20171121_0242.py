# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-21 02:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0006_auto_20171121_0152'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='case',
        ),
        migrations.RemoveField(
            model_name='history',
            name='case',
        ),
        migrations.RemoveField(
            model_name='person',
            name='case',
        ),
        migrations.AddField(
            model_name='case',
            name='binder',
            field=models.ManyToManyField(blank=True, null=True, to='cases.Binder'),
        ),
        migrations.AddField(
            model_name='case',
            name='event',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cases.Event'),
        ),
        migrations.AddField(
            model_name='case',
            name='history_log',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cases.History'),
        ),
        migrations.AddField(
            model_name='case',
            name='suspect',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='person_suspect', to='cases.Person'),
        ),
        migrations.AddField(
            model_name='case',
            name='victim',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='person_victim', to='cases.Person'),
        ),
        migrations.AlterField(
            model_name='case',
            name='related_cases',
            field=models.ManyToManyField(related_name='_case_related_cases_+', to='cases.Case'),
        ),
    ]