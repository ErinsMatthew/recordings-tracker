from django.core.management.base import BaseCommand, CommandError
from api.models import ShowFile
from django.conf import settings

import os
from api.utils import json_file_stat


def find_file(filename: str, search_path: str) -> str:
    for root, dirs, files in os.walk(search_path):
        if filename in files:
            return os.path.join(root, filename)

    return None


class Command(BaseCommand):
    help = "Updates information about ShowFiles."

    def handle(self, *args, **options):
        self.stdout.write(self.help)

        show_files = ShowFile.objects.all()

        for show_file in show_files:
            try:
                full_file_name = show_file.full_path

                # find full file in base directory if we only have base name
                if full_file_name == show_file.base_name:
                    full_file_name = find_file(
                        show_file.base_name, settings.SHOWFILES_LOCAL_BASE_DIR
                    )

                if full_file_name is not None and full_file_name != show_file.base_name:
                    if os.path.exists(full_file_name):
                        self.stdout.write(
                            self.style.SUCCESS(f"Found {full_file_name}")
                        )

                        show_file.file_size = os.path.getsize(full_file_name)
                        show_file.file_stats_json = json_file_stat(full_file_name)

                        show_file.save()

                        self.stdout.write(
                            self.style.SUCCESS(f"Updated {show_file.base_name}")
                        )

            except ShowFile.DoesNotExist:
                raise CommandError("No ShowFiles exist.")
