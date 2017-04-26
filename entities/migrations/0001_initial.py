# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-26 15:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('observations', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ParentUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identification', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('parentuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='entities.ParentUser')),
                ('specialty', models.CharField(max_length=100)),
            ],
            bases=('entities.parentuser',),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('parentuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='entities.ParentUser')),
                ('parent', models.CharField(max_length=100)),
            ],
            bases=('entities.parentuser',),
        ),
    ]
