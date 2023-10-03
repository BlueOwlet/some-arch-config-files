"""InterAct URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from users.views import Login
from students.views import Dashboard
from django.urls import path, include #add include here

from rest_framework import routers

from operation import views




router = routers.DefaultRouter()

# router.register(r'users', views.UserViewSet,basename='users')
# router.register(r'groups', views.GroupViewSet)
# router.register(r'permissions', views.PermissionViewSet)
router.register(r'api/database',views.DatabaseViewset,basename='database')
router.register(r'api/students',views.StudentsViewset,basename='students')
router.register(r'api/instructors',views.InstructorsViewset,basename='instructors')
router.register(r'api/materials',views.MaterialsViewset,basename='materials')
router.register(r'api/dashboard',views.DashboardViewset,basename='dashboard')
router.register(r'api/adminmaker',views.AdminMaker,basename='adminmaker')





urlpatterns = [

    path('api/admin/', admin.site.urls),
    path('api/auth/', include('djoser.urls')),
    path('api/auth/', include('djoser.urls.authtoken')),
    # path(r'^auth/', include('drf_social_oauth2.urls', namespace='drf'))



    path('', include(router.urls)),

]
