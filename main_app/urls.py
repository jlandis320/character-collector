from django.urls import path
from . import views 

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('characters/', views.characters_index, name='characters_index'),
    path('characters/<int:character_id>/', views.characters_detail, name='characters_detail'),
    path('characters/create/', views.CharacterCreate.as_view(), name='characters_create'),
    path('characters/<int:pk>/update', views.CharacterUpdate.as_view(), name='characters_update'),
    path('characters/<int:pk>/delete', views.CharacterDelete.as_view(), name='characters_delete'),
    path('characters/<int:character_id>/add_title/', views.add_title, name='add_title'),
    path('medium/create/', views.MediumCreate.as_view(), name='medium_create'),
    path('medium/<int:pk>/', views.MediumDetail.as_view(), name='medium_detail'),
    path('mediums/', views.MediumList.as_view(), name='medium_index'),
    path('mediums/<int:pk>/update/', views.MediumUpdate.as_view(), name='medium_update'),
    path('mediums/<int:pk>/delete/', views.MediumDelete.as_view(), name='medium_delete'),
    path('characters/<int:character_id>/assoc_medium/<int:medium_id>/', views.assoc_medium, name='assoc_medium'),
]
