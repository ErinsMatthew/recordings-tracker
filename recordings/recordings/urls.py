from django.urls import include, path
from rest_framework import routers

from api import views

router = routers.DefaultRouter()

router.register(r"users", views.UserViewSet)
router.register(r"groups", views.GroupViewSet)

router.register(r"programs", views.ProgramViewSet)
router.register(r"locations", views.LocationViewSet)
router.register(r"seasons", views.SeasonViewSet)
router.register(r"season_groups", views.SeasonGroupViewSet)
router.register(r"shows", views.ShowViewSet)
router.register(r"platforms", views.PlatformViewSet)
router.register(r"show_platforms", views.ShowPlatformViewSet)
router.register(r"equipment_types", views.EquipmentTypeViewSet)
router.register(r"equipments", views.EquipmentViewSet)
router.register(r"show_equipments", views.ShowEquipmentViewSet)
router.register(r"file_types", views.FileTypeViewSet)
router.register(r"show_files", views.ShowFileViewSet)
router.register(r"songs", views.SongViewSet)
router.register(r"show_songs", views.ShowSongViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
