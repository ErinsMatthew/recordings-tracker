from django.contrib.auth.models import Group, User
from rest_framework import serializers

from .models import (
    Equipment,
    EquipmentType,
    FileType,
    Location,
    Platform,
    Program,
    Season,
    SeasonGroup,
    Show,
    ShowEquipment,
    ShowFile,
    ShowPlatform,
    ShowSong,
    Song,
)


class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = "__all__"


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"


class SeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Season
        fields = "__all__"


class SeasonGroupSerializer(serializers.ModelSerializer):
    season = SeasonSerializer(read_only=True)

    class Meta:
        model = SeasonGroup
        fields = "__all__"


class ShowSerializer(serializers.ModelSerializer):
    full_name = serializers.ReadOnlyField()
    season_group = SeasonGroupSerializer(read_only=True)
    location = LocationSerializer(read_only=True)

    class Meta:
        model = Show
        fields = "__all__"


class PlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platform
        fields = "__all__"


class ShowPlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShowPlatform
        fields = "__all__"


class EquipmentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EquipmentType
        fields = "__all__"


class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = "__all__"


class ShowEquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShowEquipment
        fields = "__all__"


class FileTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileType
        fields = "__all__"


class ShowFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShowFile
        fields = "__all__"


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = "__all__"


class ShowSongSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShowSong
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "groups"]


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ["url", "name"]
