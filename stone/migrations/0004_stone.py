# Generated by Django 3.0 on 2019-12-16 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stone', '0003_attribute'),
    ]

    operations = [
        migrations.CreateModel(
            name='stone',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('stone_name_th', models.CharField(max_length=150)),
                ('stone_name_en', models.CharField(max_length=150)),
                ('color', models.CharField(max_length=150)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('stone_Img', models.FileField(blank=True, null=True, upload_to='stone')),
                ('attribute', models.ManyToManyField(related_name='attribute', to='stone.attribute')),
            ],
            options={
                'ordering': ['stone_name_en'],
            },
        ),
    ]
