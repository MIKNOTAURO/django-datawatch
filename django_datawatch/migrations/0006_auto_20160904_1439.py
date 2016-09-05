# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-04 14:39
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('django_datawatch', '0005_auto_20160904_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='assigned_to_group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.Group'),
        ),
        migrations.AlterField(
            model_name='result',
            name='assigned_to_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assigned_to_user', to=settings.AUTH_USER_MODEL),
        ),
    ]