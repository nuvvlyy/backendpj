# Generated by Django 3.0 on 2020-01-12 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stone', '0026_stoneimg_stoneimgsm'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stone',
            name='src_img',
        ),
        migrations.AlterField(
            model_name='stone',
            name='stone_img',
            field=models.FileField(blank=True, null=True, upload_to='stone'),
        ),
        migrations.AlterField(
            model_name='stone',
            name='stone_img_sm',
            field=models.FileField(blank=True, null=True, upload_to='stone_sm'),
        ),
    ]
