# Generated by Django 3.0 on 2020-01-12 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stone', '0031_startype_month_of_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='stone',
            name='ancient_name',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='stone',
            name='element',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
