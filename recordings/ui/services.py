from django.conf import settings

import requests


def get_url_json(url):
    response = requests.get(url, auth=(settings.USER_ID, settings.PASSWORD))

    return response.json()


def get_list(url, key):
    response_json = get_url_json(url)

    return {key: response_json["results"]}


def get_detail(url, key):
    response_json = get_url_json(url)

    return {key: response_json}


def get_programs():
    return get_list(f"{settings.API_BASE_URL}programs/", "programs")


def get_program(id):
    return get_detail(f"{settings.API_BASE_URL}programs/{id}","program")


def get_locations():
    return get_list(f"{settings.API_BASE_URL}locations/", "locations")


def get_location(id):
    return get_detail(f"{settings.API_BASE_URL}locations/{id}","location")


def get_seasons():
    return get_list(f"{settings.API_BASE_URL}seasons/", "seasons")


def get_season(id):
    return get_detail(f"{settings.API_BASE_URL}seasons/{id}","season")


def get_season_groups():
    return get_list(f"{settings.API_BASE_URL}season_groups/", "season_groups")


def get_season_group(id):
    return get_detail(f"{settings.API_BASE_URL}season_groups/{id}","season_group")


def get_shows():
    return get_list(f"{settings.API_BASE_URL}shows/", "shows")


def get_show(id):
    return get_detail(f"{settings.API_BASE_URL}shows/{id}","show")


def get_platforms():
    return get_list(f"{settings.API_BASE_URL}platforms/", "platforms")


def get_platform(id):
    return get_detail(f"{settings.API_BASE_URL}platforms/{id}","platform")


def get_show_platforms():
    return get_list(f"{settings.API_BASE_URL}show_platforms/", "show_platforms")


def get_show_platform(id):
    return get_detail(f"{settings.API_BASE_URL}show_platforms/{id}","show_platform")


def get_equipment_types():
    return get_list(f"{settings.API_BASE_URL}equipment_types/", "equipment_types")


def get_equipment_type(id):
    return get_detail(f"{settings.API_BASE_URL}equipment_types/{id}","equipment_type")


def get_equipments():
    return get_list(f"{settings.API_BASE_URL}equipments/", "equipments")


def get_equipment(id):
    return get_detail(f"{settings.API_BASE_URL}equipments/{id}","equipment")


def get_show_equipments():
    return get_list(f"{settings.API_BASE_URL}show_equipments/", "show_equipments")


def get_show_equipment(id):
    return get_detail(f"{settings.API_BASE_URL}show_equipments/{id}","show_equipment")


def get_file_types():
    return get_list(f"{settings.API_BASE_URL}file_types/", "file_types")


def get_file_type(id):
    return get_detail(f"{settings.API_BASE_URL}file_types/{id}","file_type")


def get_show_files():
    return get_list(f"{settings.API_BASE_URL}show_files/", "show_files")


def get_show_file(id):
    return get_detail(f"{settings.API_BASE_URL}show_files/{id}","show_file")


def get_songs():
    return get_list(f"{settings.API_BASE_URL}songs/", "songs")


def get_song(id):
    return get_detail(f"{settings.API_BASE_URL}songs/{id}","song")


def get_show_songs():
    return get_list(f"{settings.API_BASE_URL}show_songs/", "show_songs")


def get_show_song(id):
    return get_detail(f"{settings.API_BASE_URL}show_songs/{id}","show_song")
