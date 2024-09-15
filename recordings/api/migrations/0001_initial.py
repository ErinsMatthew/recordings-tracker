# Generated by Django 5.1.1 on 2024-09-15 22:43

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EquipmentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='FileType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('city', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('url_pattern', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('artist', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.equipmenttype')),
            ],
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('year', models.PositiveIntegerField(default=2024, validators=[django.core.validators.MinValueValidator(2019), django.core.validators.MaxValueValidator(2024)])),
                ('sequence', models.PositiveSmallIntegerField(null=True)),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.program')),
            ],
        ),
        migrations.CreateModel(
            name='SeasonGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('has_tristan', models.BooleanField(default=True)),
                ('has_erin', models.BooleanField(default=False)),
                ('season', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.season')),
            ],
        ),
        migrations.CreateModel(
            name='Show',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('date', models.DateField()),
                ('recorded', models.BooleanField(default=False)),
                ('comments', models.CharField(max_length=4096)),
                ('sequence', models.PositiveSmallIntegerField(null=True)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.location')),
                ('season_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.seasongroup')),
            ],
        ),
        migrations.CreateModel(
            name='ShowEquipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equipment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.equipment')),
                ('show', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.show')),
            ],
            options={
                'unique_together': {('show', 'equipment')},
            },
        ),
        migrations.CreateModel(
            name='ShowFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_path', models.CharField(max_length=4096)),
                ('base_name', models.CharField(max_length=4096)),
                ('sequence', models.PositiveSmallIntegerField(null=True)),
                ('icloud_local_path', models.CharField(max_length=4096)),
                ('icloud_url', models.URLField()),
                ('file_size', models.PositiveIntegerField()),
                ('file_stats_json', models.JSONField()),
                ('equipment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.equipment')),
                ('file_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.filetype')),
                ('show', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.show')),
            ],
            options={
                'unique_together': {('show', 'full_path')},
            },
        ),
        migrations.CreateModel(
            name='ShowPlatform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=64)),
                ('platform', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.platform')),
                ('show', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.show')),
            ],
            options={
                'unique_together': {('show', 'platform')},
            },
        ),
        migrations.CreateModel(
            name='ShowSong',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('has_tristan', models.BooleanField(default=False)),
                ('has_erin', models.BooleanField(default=False)),
                ('start_seconds', models.PositiveSmallIntegerField(null=True)),
                ('show', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.show')),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.song')),
            ],
            options={
                'unique_together': {('show', 'song')},
            },
        ),
    ]
