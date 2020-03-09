# Generated by Django 3.0 on 2020-03-09 07:50

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stone', '0036_auto_20200204_0723'),
    ]

    operations = [
        migrations.AddField(
            model_name='stone',
            name='notusewith',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), default=list, size=None),
        ),
        migrations.AlterField(
            model_name='stone',
            name='attribute',
            field=models.ManyToManyField(blank=True, null=True, related_name='attribute', to='stone.Attribute'),
        ),
    ]