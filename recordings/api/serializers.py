from argparse import FileType
from django.contrib.auth.models import Group, User
from rest_framework import serializers

from .models import (
    Equipment,
    EquipmentType,
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


class ProgramSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Program
        fields = "__all__"


class LocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"


class SeasonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Season
        fields = "__all__"


class SeasonGroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SeasonGroup
        fields = "__all__"


class ShowSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Show
        fields = "__all__"


class PlatformSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Platform
        fields = "__all__"


class ShowPlatformSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ShowPlatform
        fields = "__all__"


class EquipmentTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EquipmentType
        fields = "__all__"


class EquipmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Equipment
        fields = "__all__"


class ShowEquipmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ShowEquipment
        fields = "__all__"


class FileTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FileType
        fields = "__all__"


class ShowFileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ShowFile
        fields = "__all__"


class SongSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Song
        fields = "__all__"


class ShowSongSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ShowSong
        fields = "__all__"


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "groups"]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ["url", "name"]
