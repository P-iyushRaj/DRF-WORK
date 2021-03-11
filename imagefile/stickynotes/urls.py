from django.contrib import admin
from django.urls import path, include
from app import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('notesapi', views.NotesView,
basename='Notes')

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

