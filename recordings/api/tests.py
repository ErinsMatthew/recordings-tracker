from django.test import TestCase

from .models import Location, Program, Season


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
