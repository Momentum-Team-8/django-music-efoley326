from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from musicApp import views as albums_views


urlpatterns = [
path('admin/', admin.site.urls),
    path('', albums_views.list_albums, name='list_albums'),
    path('albums/add/', albums_views.add_album, name='add_album'),
    path('albums/<int:pk>/edit/', albums_views.edit_album, name='edit_album'),
    path('albums/<int:pk>/delete/', albums_views.delete_album, name='delete_album'),
]





