from django.test import TestCase

import datetime

from api.utils import json_file_stat

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


class TestData:
    strings = {
        "program_name": "Test Program Name",
        "season_name": "Test Season Name",
        "season_group_name": "Test SeasonGroup Name",
        "location_name": "Test Location Name",
        "city_name": "Test Location City",
        "show_name": "Test Show Name",
        "platform_name": "Test Platform Name",
        "equipment_type_name": "Test EquipmentType Name",
        "equipment_name": "Test Equipment Name",
        "file_type_name": "Test FileType Name",
        "song_name": "Test Song Name",
        "artist_name": "Test Artist Name",
    }

    program = Program(name=strings["program_name"])

    season = Season(
        name=strings["season_name"],
        program=program,
        year=datetime.date.today().year,
        sequence=1,
    )

    season_group = SeasonGroup(
        season=season,
        name=strings["season_group_name"],
        has_tristan=True,
        has_erin=False,
    )

    location = Location(name=strings["location_name"], city=strings["city_name"])

    show = Show(
        name=strings["show_name"],
        season_group=season_group,
        date=datetime.date.today(),
        location=location,
        recorded=True,
        comments="Sample Comments",
        sequence=1,
    )

    platform = Platform(
        name=strings["platform_name"],
        url_pattern="https://youtube.com/watch?v=%s",
    )

    show_platform = ShowPlatform(
        show=show,
        platform=platform,
        key="abc1234",
    )

    equipment_type = EquipmentType(name=strings["equipment_type_name"])

    equipment = Equipment(name=strings["equipment_name"], type=equipment_type)

    show_equipment = ShowEquipment(show=show, equipment=equipment)

    file_type = FileType(name=strings["file_type_name"])

    show_file = ShowFile(
        show=show,
        full_path="Full Path to File",
        base_name="Base Name of File",
        file_type=file_type,
        equipment=equipment,
        sequence=1,
        icloud_local_path="../README.md",
        icloud_url="https://www.icloud.com/path/to/file",
        file_size=0,
        file_stats_json=json_file_stat("../README.md"),
    )

    song = Song(name=strings["song_name"], artist=strings["artist_name"])

    show_song = ShowSong(
        show=show,
        song=song,
        has_tristan=True,
        has_erin=False,
        start_seconds=0,
    )


test_data = TestData()


class ProgramModelTests(TestCase):
    def test_name(self):
        self.assertIs(test_data.program.name, test_data.strings["program_name"])


class LocationModelTests(TestCase):
    def test_name(self):
        self.assertIs(test_data.location.name, test_data.strings["location_name"])


class SeasonModelTests(TestCase):
    def test_name(self):
        self.assertIs(test_data.season.name, test_data.strings["season_name"])


class SeasonGroupModelTests(TestCase):
    def test_name(self):
        self.assertIs(
            test_data.season_group.name, test_data.strings["season_group_name"]
        )


class ShowModelTests(TestCase):
    def test_name(self):
        self.assertIs(test_data.show.name, test_data.strings["show_name"])


class PlatformModelTests(TestCase):
    def test_name(self):
        self.assertIs(test_data.platform.name, test_data.strings["platform_name"])


class ShowPlatformModelTests(TestCase):
    def test_name(self):
        self.assertIs(
            test_data.show_platform.platform.name, test_data.strings["platform_name"]
        )


class EquipmentTypeModelTests(TestCase):
    def test_name(self):
        self.assertIs(
            test_data.equipment_type.name, test_data.strings["equipment_type_name"]
        )


class EquipmentModelTests(TestCase):
    def test_name(self):
        self.assertIs(test_data.equipment.name, test_data.strings["equipment_name"])


class ShowEquipmentModelTests(TestCase):
    def test_name(self):
        self.assertIs(
            test_data.show_equipment.show.name, test_data.strings["show_name"]
        )


class FileTypeModelTests(TestCase):
    def test_name(self):
        self.assertIs(test_data.file_type.name, test_data.strings["file_type_name"])


class ShowFileModelTests(TestCase):
    def test_name(self):
        self.assertIs(test_data.show_file.full_path, "Full Path to File")

    def test_json(self):
        self.assertRegex(test_data.show_file.file_stats_json, ".*{.*")


class SongModelTests(TestCase):
    def test_name(self):
        self.assertIs(test_data.song.name, test_data.strings["song_name"])


class ShowSongModelTests(TestCase):
    def test_name(self):
        self.assertIs(test_data.show_song.song.name, test_data.strings["song_name"])
