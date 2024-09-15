from api import utils
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

import datetime

current_year = datetime.date.today().year


class Program(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(max_length=128)
    city = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.name} ({self.city})"


class Season(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    year = models.PositiveIntegerField(
        default=current_year,
        validators=[MinValueValidator(2019), MaxValueValidator(current_year)],
    )
    sequence = models.PositiveSmallIntegerField(null=True)

    def __str__(self):
        return self.name


class SeasonGroup(models.Model):
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    has_tristan = models.BooleanField(default=True)
    has_erin = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.season.name}"


class Show(models.Model):
    name = models.CharField(max_length=128)
    season_group = models.ForeignKey(SeasonGroup, on_delete=models.CASCADE)
    date = models.DateField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    recorded = models.BooleanField(default=False)
    comments = models.CharField(max_length=4096)
    sequence = models.PositiveSmallIntegerField(null=True)

    def __str__(self):
        return self.name


class Platform(models.Model):
    name = models.CharField(max_length=128)
    url_pattern = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class ShowPlatform(models.Model):
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE)
    key = models.CharField(max_length=64)

    def __str__(self):
        return utils.object_to_json(self)

    class Meta:
        unique_together = ["show", "platform"]


class EquipmentType(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Equipment(models.Model):
    name = models.CharField(max_length=128)
    type = models.ForeignKey(EquipmentType, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.type})"


class ShowEquipment(models.Model):
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)

    def __str__(self):
        return utils.object_to_json(self)

    class Meta:
        unique_together = ["show", "equipment"]


class FileType(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class ShowFile(models.Model):
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    full_path = models.CharField(max_length=4096)  # see PATH_MAX in <linux/limits.h>
    base_name = models.CharField(max_length=4096)
    file_type = models.ForeignKey(FileType, on_delete=models.CASCADE)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    sequence = models.PositiveSmallIntegerField(null=True)
    icloud_local_path = models.CharField(
        max_length=4096
    )  # see PATH_MAX in <linux/limits.h>
    icloud_url = models.URLField()
    file_size = models.PositiveIntegerField()
    file_stats_json = models.JSONField()

    def __str__(self):
        return utils.object_to_json(self)

    class Meta:
        unique_together = ["show", "full_path"]


class Song(models.Model):
    name = models.CharField(max_length=128)
    artist = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.name} ({self.artist})"


class ShowSong(models.Model):
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    has_tristan = models.BooleanField(default=False)
    has_erin = models.BooleanField(default=False)
    start_seconds = models.PositiveSmallIntegerField(null=True)

    def __str__(self):
        return self.show.name
    
    class Meta:
        unique_together = ["show", "song"]