from django.urls import include, path
from rest_framework import routers

from api import views as apiviews
from ui import views as uiviews

router = routers.DefaultRouter()

router.register(r"users", apiviews.UserViewSet)
router.register(r"groups", apiviews.GroupViewSet)

router.register(r"programs", apiviews.ProgramViewSet)
router.register(r"locations", apiviews.LocationViewSet)
router.register(r"seasons", apiviews.SeasonViewSet)
router.register(r"season_groups", apiviews.SeasonGroupViewSet)
router.register(r"shows", apiviews.ShowViewSet)
router.register(r"platforms", apiviews.PlatformViewSet)
router.register(r"show_platforms", apiviews.ShowPlatformViewSet)
router.register(r"equipment_types", apiviews.EquipmentTypeViewSet)
router.register(r"equipments", apiviews.EquipmentViewSet)
router.register(r"show_equipments", apiviews.ShowEquipmentViewSet)
router.register(r"file_types", apiviews.FileTypeViewSet)
router.register(r"show_files", apiviews.ShowFileViewSet)
router.register(r"songs", apiviews.SongViewSet)
router.register(r"show_songs", apiviews.ShowSongViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("", include(router.urls)),
    path("ui/", uiviews.index, name="index"),
    path("ui/programs/", uiviews.programs, name="programs"),
    path("ui/programs/<int:id>/", uiviews.program, name="program"),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
