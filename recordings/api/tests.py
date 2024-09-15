from django.test import TestCase

import datetime

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


class ProgramModelTests(TestCase):
    def test_name(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        program = Program(name="Test Program Name")

        self.assertIs(program.name, "Test Program Name")


class LocationModelTests(TestCase):
    def test_name(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        location = Location(name="Test Location Name", city="Test Location City")

        self.assertIs(location.name, "Test Location Name")


class SeasonModelTests(TestCase):
    def test_name(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        program = Program(name="Test Program Name")

        season = Season(name="Test Season Name", program=program, year=2024, sequence=1)

        self.assertIs(season.name, "Test Season Name")


class SeasonGroupModelTests(TestCase):
    def test_name(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        program = Program(name="Test Program Name")

        season = Season(name="Test Season Name", program=program, year=2024, sequence=1)

        season_group = SeasonGroup(
            season=season,
            group_name="Test Group Name",
            has_tristan=True,
            has_erin=False,
        )

        self.assertIs(season_group.group_name, "Test Group Name")


class ShowModelTests(TestCase):
    def test_name(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        location = Location(name="Test Location Name", city="Test Location City")

        program = Program(name="Test Program Name")

        season = Season(name="Test Season Name", program=program, year=2024, sequence=1)

        season_group = SeasonGroup(
            season=season,
            group_name="Test Group Name",
            has_tristan=True,
            has_erin=False,
        )

        show = Show(
            name="Test Show Name",
            season_group=season_group,
            show_date=datetime.date.today(),
            location=location,
            was_recorded=True,
            comments="",
            sequence=1,
        )

        self.assertIs(show.name, "Test Show Name")


class PlatformModelTests(TestCase):
    def test_name(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        platform = Platform(name="Test Platform Name", url_pattern="")

        self.assertIs(platform.name, "Test Platform Name")


class ShowPlatformModelTests(TestCase):
    def test_name(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        location = Location(name="Test Location Name", city="Test Location City")

        program = Program(name="Test Program Name")

        season = Season(name="Test Season Name", program=program, year=2024, sequence=1)

        season_group = SeasonGroup(
            season=season,
            group_name="Test Group Name",
            has_tristan=True,
            has_erin=False,
        )

        show = Show(
            name="Test Show Name",
            season_group=season_group,
            show_date=datetime.date.today(),
            location=location,
            was_recorded=True,
            comments="",
            sequence=1,
        )

        platform = Platform(name="Test Platform Name", url_pattern="")

        show_platform = ShowPlatform(show=show, platform=platform, key="")

        self.assertIs(show_platform.platform.name, "Test Platform Name")


class EquipmentTypeModelTests(TestCase):
    def test_name(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        equipment_type = EquipmentType(name="Test EquipmentType Name")

        self.assertIs(equipment_type.name, "Test EquipmentType Name")


class EquipmentModelTests(TestCase):
    def test_name(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        equipment_type = EquipmentType(name="Test EquipmentType Name")

        equipment = Equipment(name="Test Equipment Name", type=equipment_type)

        self.assertIs(equipment.name, "Test Equipment Name")


class ShowEquipmentModelTests(TestCase):
    def test_name(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        location = Location(name="Test Location Name", city="Test Location City")

        program = Program(name="Test Program Name")

        season = Season(name="Test Season Name", program=program, year=2024, sequence=1)

        season_group = SeasonGroup(
            season=season,
            group_name="Test Group Name",
            has_tristan=True,
            has_erin=False,
        )

        show = Show(
            name="Test Show Name",
            season_group=season_group,
            show_date=datetime.date.today(),
            location=location,
            was_recorded=True,
            comments="",
            sequence=1,
        )

        equipment_type = EquipmentType(name="Test EquipmentType Name")

        equipment = Equipment(name="Test Equipment Name", type=equipment_type)

        show_equipment = ShowEquipment(show=show, equipment=equipment)

        self.assertIs(show_equipment.show.name, "Test Show Name")


class FileTypeModelTests(TestCase):
    def test_name(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        file_type = FileType(name="Test FileType Name")

        self.assertIs(file_type.name, "Test FileType Name")


class ShowFileModelTests(TestCase):
    def test_name(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        file_type = FileType(name="Test FileType Name")

        equipment_type = EquipmentType(name="Test EquipmentType Name")

        equipment = Equipment(name="Test Equipment Name", type=equipment_type)

        location = Location(name="Test Location Name", city="Test Location City")

        program = Program(name="Test Program Name")

        season = Season(name="Test Season Name", program=program, year=2024, sequence=1)

        season_group = SeasonGroup(
            season=season,
            group_name="Test Group Name",
            has_tristan=True,
            has_erin=False,
        )

        show = Show(
            name="Test Show Name",
            season_group=season_group,
            show_date=datetime.date.today(),
            location=location,
            was_recorded=True,
            comments="",
            sequence=1,
        )

        show_file = ShowFile(
            show=show,
            full_path="Full Path to File",
            base_name="",
            file_type=file_type,
            equipment=equipment,
            sequence=1,
            icloud_local_path="",
            icloud_url="",
            file_size=0,
            file_metadata_json="{}",
        )

        self.assertIs(show_file.full_path, "Full Path to File")


class SongModelTests(TestCase):
    def test_name(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        song = Song(name="Test Song Name", artist="Test Artist Name")

        self.assertIs(song.name, "Test Song Name")


class ShowSongModelTests(TestCase):
    def test_name(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        location = Location(name="Test Location Name", city="Test Location City")

        program = Program(name="Test Program Name")

        season = Season(name="Test Season Name", program=program, year=2024, sequence=1)

        season_group = SeasonGroup(
            season=season,
            group_name="Test Group Name",
            has_tristan=True,
            has_erin=False,
        )

        show = Show(
            name="Test Show Name",
            season_group=season_group,
            show_date=datetime.date.today(),
            location=location,
            was_recorded=True,
            comments="",
            sequence=1,
        )

        song = Song(name="Test Song Name", artist="Test Artist Name")

        show_song = ShowSong(
            show=show,
            song=song,
            has_tristan=True,
            has_erin=False,
            start_seconds=0,
        )

        self.assertIs(show_song.song.name, "Test Song Name")
