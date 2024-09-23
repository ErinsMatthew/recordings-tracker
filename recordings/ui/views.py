from django.shortcuts import render

from ui import services


def index(request):
    return render(request, "ui/index.html")


def programs(request):
    programs_list = services.get_programs()

    return render(request, "ui/programs.html", programs_list)


def program(request, id):
    program_dict = services.get_program(id)

    return render(request, "ui/program.html", program_dict)


def locations(request):
    locations_obj = services.get_locations()

    return render(request, "ui/locations.html", locations_obj)


def location(request, id):
    location_obj = services.get_location(id)

    return render(request, "ui/location.html", location_obj)


def seasons(request):
    seasons_obj = services.get_seasons()

    return render(request, "ui/seasons.html", seasons_obj)


def season(request, id):
    season_obj = services.get_season(id)

    return render(request, "ui/season.html", season_obj)


def season_groups(request):
    season_groups_obj = services.get_season_groups()

    return render(request, "ui/season_groups.html", season_groups_obj)


def season_group(request, id):
    season_group_obj = services.get_season_group(id)

    return render(request, "ui/season_group.html", season_group_obj)


def shows(request):
    shows_obj = services.get_shows()

    return render(request, "ui/shows.html", shows_obj)


def show(request, id):
    show_obj = services.get_show(id)

    return render(request, "ui/show.html", show_obj)


def platforms(request):
    platforms_obj = services.get_platforms()

    return render(request, "ui/platforms.html", platforms_obj)


def platform(request, id):
    platform_obj = services.get_platform(id)

    return render(request, "ui/platform.html", platform_obj)


def show_platforms(request):
    show_platforms_obj = services.get_show_platforms()

    return render(request, "ui/show_platforms.html", show_platforms_obj)


def show_platform(request, id):
    show_platform_obj = services.get_show_platform(id)

    return render(request, "ui/show_platform.html", show_platform_obj)


def equipment_types(request):
    equipment_types_obj = services.get_equipment_types()

    return render(request, "ui/equipment_types.html", equipment_types_obj)


def equipment_type(request, id):
    equipment_type_obj = services.get_equipment_type(id)

    return render(request, "ui/equipment_type.html", equipment_type_obj)


def equipments(request):
    equipments_obj = services.get_equipments()

    return render(request, "ui/equipments.html", equipments_obj)


def equipment(request, id):
    equipment_obj = services.get_equipment(id)

    return render(request, "ui/equipment.html", equipment_obj)


def show_equipments(request):
    show_equipments_obj = services.get_show_equipments()

    return render(request, "ui/show_equipments.html", show_equipments_obj)


def show_equipment(request, id):
    show_equipment_obj = services.get_show_equipment(id)

    return render(request, "ui/show_equipment.html", show_equipment_obj)


def file_types(request):
    file_types_obj = services.get_file_types()

    return render(request, "ui/file_types.html", file_types_obj)


def file_type(request, id):
    file_type_obj = services.get_file_type(id)

    return render(request, "ui/file_type.html", file_type_obj)


def show_files(request):
    show_files_obj = services.get_show_files()

    return render(request, "ui/show_files.html", show_files_obj)


def show_file(request, id):
    show_file_obj = services.get_show_file(id)

    return render(request, "ui/show_file.html", show_file_obj)


def songs(request):
    songs_obj = services.get_songs()

    return render(request, "ui/songs.html", songs_obj)


def song(request, id):
    song_obj = services.get_song(id)

    return render(request, "ui/song.html", song_obj)


def show_songs(request):
    show_songs_obj = services.get_show_songs()

    return render(request, "ui/show_songs.html", show_songs_obj)


def show_song(request, id):
    show_song_obj = services.get_show_song(id)

    return render(request, "ui/show_song.html", show_song_obj)
