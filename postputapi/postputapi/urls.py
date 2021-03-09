from django.contrib import admin
from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

#register viewset using router
# url http://127.0.0.1:8000/studentapi
router.register('studentapi', views.StudentModelViewSet,
basename='Student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]

#post http://127.0.0.1:8000/studentapi/
#put http://127.0.0.1:8000/studentapi/1/