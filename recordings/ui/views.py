import requests

from django.shortcuts import render

from django.conf import settings


def index(request):
    response = requests.get(
        "http://127.0.0.1:8000/platforms/", auth=(settings.USERID, settings.PASSWORD)
    )

    platforms = response.json()["results"]

    return render(request, "ui/platforms.html", {"platforms": platforms})
