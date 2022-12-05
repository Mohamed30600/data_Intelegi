from django.urls import path
from . import views

urlpatterns = [
    path('', views.readtable, name='readtable'),
    path('add/', views.add, name='add'),
    path('add/addrecord/', views.addrecord, name='addrecord'),
    path('delete/<pvalmin>', views.delete, name='delete'),
    
]
