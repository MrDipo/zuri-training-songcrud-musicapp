from django.urls import include, path

from rest_framework import routers

from gbedu.views import ArtisteViewSet, SongViewSet, LyricViewSet

router = routers.DefaultRouter()
router.register(r'artistes', ArtisteViewSet)
router.register(r'songs', SongViewSet)
router.register(r'lyrics', LyricViewSet)

urlpatterns = [
   path('', include(router.urls)),
]