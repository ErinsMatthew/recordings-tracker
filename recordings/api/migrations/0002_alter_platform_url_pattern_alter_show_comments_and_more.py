# Generated by Django 5.1.1 on 2024-09-23 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='platform',
            name='url_pattern',
            field=models.CharField(default='', max_length=256),
        ),
        migrations.AlterField(
            model_name='show',
            name='comments',
            field=models.CharField(default='', max_length=4096),
        ),
        migrations.AlterField(
            model_name='showfile',
            name='icloud_local_path',
            field=models.CharField(default='', max_length=4096),
        ),
        migrations.AlterField(
            model_name='showfile',
            name='icloud_url',
            field=models.URLField(default=''),
        ),
    ]
