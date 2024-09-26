from django.urls import include, path
from rest_framework import routers

from api import views as apiviews
from ui import views as uiviews

router = routers.DefaultRouter()

router.register("users", apiviews.UserViewSet)
router.register("groups", apiviews.GroupViewSet)

router.register("programs", apiviews.ProgramViewSet)
router.register("locations", apiviews.LocationViewSet)
router.register("seasons", apiviews.SeasonViewSet)
router.register("season_groups", apiviews.SeasonGroupViewSet)
router.register("shows", apiviews.ShowViewSet)
router.register("platforms", apiviews.PlatformViewSet)
router.register("show_platforms", apiviews.ShowPlatformViewSet)
router.register("equipment_types", apiviews.EquipmentTypeViewSet)
router.register("equipments", apiviews.EquipmentViewSet)
router.register("show_equipments", apiviews.ShowEquipmentViewSet)
router.register("file_types", apiviews.FileTypeViewSet)
router.register("show_files", apiviews.ShowFileViewSet)
router.register("songs", apiviews.SongViewSet)
router.register("show_songs", apiviews.ShowSongViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("_api/", include(router.urls)),
    path("", uiviews.index, name="index"),
    path("programs/", uiviews.programs, name="programs"),
    path("programs/<int:id>/", uiviews.program, name="program"),
    path("locations/", uiviews.locations, name="locations"),
    path("locations/<int:id>/", uiviews.location, name="location"),
    path("seasons/", uiviews.seasons, name="seasons"),
    path("seasons/<int:id>/", uiviews.season, name="season"),
    path("season_groups/", uiviews.season_groups, name="season_groups"),
    path("season_groups/<int:id>/", uiviews.season_group, name="season_group"),
    # path("shows/", uiviews.shows, name="shows"),
    path("shows/", uiviews.ShowListView.as_view(), name="shows"),
    path("shows/<int:id>/", uiviews.show, name="show"),
    path("platforms/", uiviews.platforms, name="platforms"),
    path("platforms/<int:id>/", uiviews.platform, name="platform"),
    path("show_platforms/", uiviews.show_platforms, name="show_platforms"),
    path("show_platforms/<int:id>/", uiviews.show_platform, name="show_platform"),
    path("equipment_types/", uiviews.equipment_types, name="equipment_types"),
    path("equipment_types/<int:id>/", uiviews.equipment_type, name="equipment_type"),
    path("equipments/", uiviews.equipments, name="equipments"),
    path("equipments/<int:id>/", uiviews.equipment, name="equipment"),
    path("show_equipments/", uiviews.show_equipments, name="show_equipments"),
    path("show_equipments/<int:id>/", uiviews.show_equipment, name="show_equipment"),
    path("file_types/", uiviews.file_types, name="file_types"),
    path("file_types/<int:id>/", uiviews.file_type, name="file_type"),
    path("show_files/", uiviews.show_files, name="show_files"),
    path("show_files/<int:id>/", uiviews.show_file, name="show_file"),
    path("songs/", uiviews.songs, name="songs"),
    path("songs/<int:id>/", uiviews.song, name="song"),
    path("show_songs/", uiviews.show_songs, name="show_songs"),
    path("show_songs/<int:id>/", uiviews.show_song, name="show_song"),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
