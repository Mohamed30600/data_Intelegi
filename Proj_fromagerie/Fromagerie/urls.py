"""Fromagerie URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path


from Gestion_communes.views import ListcommuneView,CreateCommuneView, updateCommuneView,deleteCommuneView
from Gestion_conditionnement.views import ListConditionnementView,CreateConditionnementView,updateConditionnementView,deleteConditionnementView
from Gestion_objets.views import ListObjet,CreateOnjetView,updateObjetView,deleteObjetView
import Authentification.views
from Gestion_poids.views import ListPoid,CreatePoidView,CreatePoidView,updatePoidView,deletePoidView
from Gestion_poids.views import ListPoidv,CreatePoidvView,updatePoidvView,deletePoidvView

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.urls import re_path




schema_view = get_schema_view(
   openapi.Info(
      title="Fromagerie API",
      default_version='v1',
      description="Test description",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    # path('api_schema',get_schema_view(title='API schema',description="fromagerie avec api "),name="api_schema"),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
   
    path('admin/', admin.site.urls),
    path('login/', Authentification.views.login_page, name='login'),
    path('signup/',Authentification.views.signup_page,name = 'signup'),
    path('listCommunes/',ListcommuneView.as_view(),name='listecommune'),
    path('addCommune/',CreateCommuneView.as_view(),name='add_commune'),
    path('updateCommune/<pk>/',updateCommuneView.as_view(),name='update_commune'),
    path('deleteCommune/<pk>/',deleteCommuneView.as_view(),name='delete_commune'),
    path('listConditionement/',ListConditionnementView.as_view(),name='listecommune'),
    path('addConditionement/',CreateConditionnementView.as_view(),name='add_commune'),
    path('updateConditionnement/<pk>/',updateConditionnementView.as_view(),name='update_commune'),
    path('deleteConditionement/<pk>/',deleteConditionnementView.as_view(),name='delete_commune'),
    path('listObjet/',ListObjet.as_view(),name='listecommune'),
    path('addObjet/',CreateOnjetView.as_view(),name='add_commune'),
    path('updateObjet/<pk>/',updateObjetView.as_view(),name='update_commune'),
    path('deleteObjet/<pk>/',deleteObjetView.as_view(),name='delete_commune'),
    path('listPoid/',ListPoid.as_view(),name='listPoid'),
    path('addPoid/',CreatePoidView.as_view(),name='add_commune'),
    path('updatePoid/<pk>/',updatePoidView.as_view(),name='addPoid'),
    path('deletePoid/<pk>/',deletePoidView.as_view(),name='deletePoid'),
    path('listPoidv/',ListPoidv.as_view(),name='listPoidv'),
    path('addPoidv/',CreatePoidvView.as_view(),name='addPoidv'),
    path('updatePoidv/<pk>/',updatePoidvView.as_view(),name='updatePoidv'),
    path('deletePoidv/<pk>/',deletePoidvView.as_view(),name='deletePoidv'),
    
    
    
]
