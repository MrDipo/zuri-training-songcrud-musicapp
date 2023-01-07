from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('create-artiste', views.create_artiste, name="create"),
    path('show-artistes', views.show_artistes, name="show"),
    path('edit-artiste/<int:id>', views.edit_artistes, name="edit"),
    path('update-artiste/<int:id>', views.update_artiste, name="update"),
    path('delete-artiste/<int:id>', views.destroy_artiste, name="delete"),
]
