# Generated by Django 3.0 on 2020-01-08 10:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stone', '0014_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favorite',
            name='Stone',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stone.stone'),
        ),
        migrations.AlterField(
            model_name='favorite',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
