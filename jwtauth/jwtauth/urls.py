
from django.contrib import admin
from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView, TokenVerifyView

router = DefaultRouter()

#register viewset using router
# url http://127.0.0.1:8000/studentapi
router.register('studentapi', views.StudentModelViewSet,
basename='Student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    #path('auth/', include('rest_framework.urls', namespace = 'rest_framework')),

    path('gettoken/',TokenObtainPairView.as_view(), name='token_obtain_pair'),
    #http POST http://127.0.0.1:8000/gettoken/ username="piyush" password="123456"
    path('refreshtoken/',TokenRefreshView.as_view(), name='token_refresh'),
    #http POST http://127.0.0.1:8000/refreshtoken/ refresh"refresh token here"
    path('verifytoken/',TokenVerifyView.as_view(), name='token_verify'),
    #http POST http://127.0.0.1:8000/verifytoken/ token="eyJ0e"

]

#token valid for 5min
#refreshtoken valid for 1day

#get data
#http http://127.0.0.1:8000/studentapi/ 'Authorization:Bearer ____token'
#incert data
#http -f POST http://127.0.0.1:8000/studentapi/ name="ram" roll=12 city="bhagalpur" 'Authorization:Bearer _________token' 
 


