from django.urls import path
from . import views

app_name = 'Gestion_poids'

urlpatterns = [
    path('', views.affiche_table, name='affiche_table'),
    path('ajout/', views.ajout, name='ajout'),
    path('ajout/ajout_saisi_donnees/', views.ajout_saisi_donnees, name='ajout_saisi_donnees'),
    path('delete/<pvalmin>', views.delete, name='delete'),
    path('modif/<pvalmin>', views.modif, name='modif'),
    path('modif/update_record/', views.update_record, name='update_record'),
    
]
