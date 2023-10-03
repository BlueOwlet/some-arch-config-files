from django.contrib import admin
from users.views import Login
from students.views import Dashboard
from django.urls import path, include #add include here

from rest_framework import routers

from operation import views


router = routers.DefaultRouter()



router.register(r'api/test',views.DatabaseViewset,basename='test')



urlpatterns = [

    path('api/admin/', admin.site.urls),
    path('api/auth/', include('djoser.urls')),
    path('api/auth/', include('djoser.urls.authtoken')),
    # path(r'^auth/', include('drf_social_oauth2.urls', namespace='drf'))



    path('', include(router.urls)),
]