# Generated by Django 3.0 on 2019-12-16 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('stone', '0002_auto_20191216_1957'),
    ]

    operations = [
        migrations.CreateModel(
            name='attribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute_name', models.CharField(blank=True, max_length=150, null=True)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
