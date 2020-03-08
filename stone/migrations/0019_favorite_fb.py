# Generated by Django 3.0 on 2020-01-08 16:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stone', '0018_auto_20200108_1627'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorite_FB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Stone', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='fb_stone', to='stone.stone')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stone.FaceBookUserProfile')),
            ],
        ),
    ]
