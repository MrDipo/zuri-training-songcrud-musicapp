from django.urls import include, path
from . import views
# from rest_framework import routers
# from gbedu.views import ArtisteViewSet, SongViewSet, LyricViewSet

# router = routers.DefaultRouter()
# router.register(r'artistes', ArtisteViewSet)
# router.register(r'songs', SongViewSet)
# router.register(r'lyrics', LyricViewSet)

urlpatterns = [
   # path('', include(router.urls)),
   path('', views.gbeduOverview, name='home'),
   path('create/', views.add_artistes, name='add-artistes'),
   path('all/', views.view_artistes, name='view_artistes'),
   path('update/<int:pk>/', views.update_artistes, name='update-artistes'),
]