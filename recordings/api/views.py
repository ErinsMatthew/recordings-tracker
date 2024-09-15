from django.contrib.auth.models import Group, User

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

from rest_framework import permissions, viewsets

from .serializers import (
    EquipmentSerializer,
    EquipmentTypeSerializer,
    FileTypeSerializer,
    LocationSerializer,
    PlatformSerializer,
    GroupSerializer,
    ProgramSerializer,
    SeasonGroupSerializer,
    SeasonSerializer,
    ShowEquipmentSerializer,
    ShowFileSerializer,
    ShowPlatformSerializer,
    ShowSerializer,
    ShowSongSerializer,
    SongSerializer,
    UserSerializer,
)


class ProgramViewSet(viewsets.ModelViewSet):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer
    permission_classes = [permissions.IsAuthenticated]


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [permissions.IsAuthenticated]


class SeasonViewSet(viewsets.ModelViewSet):
    queryset = Season.objects.all()
    serializer_class = SeasonSerializer
    permission_classes = [permissions.IsAuthenticated]


class SeasonGroupViewSet(viewsets.ModelViewSet):
    queryset = SeasonGroup.objects.all()
    serializer_class = SeasonGroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class ShowViewSet(viewsets.ModelViewSet):
    queryset = Show.objects.all().order_by("date")
    serializer_class = ShowSerializer
    permission_classes = [permissions.IsAuthenticated]


class PlatformViewSet(viewsets.ModelViewSet):
    queryset = Platform.objects.all()
    serializer_class = PlatformSerializer
    permission_classes = [permissions.IsAuthenticated]


class ShowPlatformViewSet(viewsets.ModelViewSet):
    queryset = ShowPlatform.objects.all()
    serializer_class = ShowPlatformSerializer
    permission_classes = [permissions.IsAuthenticated]


class EquipmentTypeViewSet(viewsets.ModelViewSet):
    queryset = EquipmentType.objects.all()
    serializer_class = EquipmentTypeSerializer
    permission_classes = [permissions.IsAuthenticated]


class EquipmentViewSet(viewsets.ModelViewSet):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
    permission_classes = [permissions.IsAuthenticated]


class ShowEquipmentViewSet(viewsets.ModelViewSet):
    queryset = ShowEquipment.objects.all()
    serializer_class = ShowEquipmentSerializer
    permission_classes = [permissions.IsAuthenticated]


class FileTypeViewSet(viewsets.ModelViewSet):
    queryset = FileType.objects.all()
    serializer_class = FileTypeSerializer
    permission_classes = [permissions.IsAuthenticated]


class ShowFileViewSet(viewsets.ModelViewSet):
    queryset = ShowFile.objects.all()
    serializer_class = ShowFileSerializer
    permission_classes = [permissions.IsAuthenticated]


class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    permission_classes = [permissions.IsAuthenticated]


class ShowSongViewSet(viewsets.ModelViewSet):
    queryset = ShowSong.objects.all()
    serializer_class = ShowSongSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
