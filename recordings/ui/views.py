from django.shortcuts import render

from ui import services


def index(request):
    programs_list = services.get_programs()

    return render(request, "ui/programs.html", programs_list)


def programs(request):
    programs_list = services.get_programs()

    return render(request, "ui/programs.html", programs_list)


def program(request, id):
    program_dict = services.get_program(id)

    return render(request, "ui/program.html", program_dict)
