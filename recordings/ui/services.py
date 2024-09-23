from django.conf import settings

import requests


def get_programs():
    response = requests.get(
        "http://127.0.0.1:8000/programs/", auth=(settings.USER_ID, settings.PASSWORD)
    )

    programs = response.json()

    return {"programs": programs["results"]}


def get_program(id):
    response = requests.get(
        f"http://127.0.0.1:8000/programs/{id}",
        auth=(settings.USER_ID, settings.PASSWORD),
    )

    program = response.json()

    return {"program": program}
