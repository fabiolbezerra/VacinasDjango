from django.urls import path
from . import views


app_name = 'pets'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    # path('', views.index, name="index"),
    path('animais/raca/<str:raca>/', views.AnimaisDaRacaView.as_view(), name="animais_raca"),
    # path('animais/raca/<str:raca>/', views.animais_raca, name="animais_raca"),
    path('animal/<int:pk>/', views.AnimalView.as_view(), name="animal_detail"),
    # path('animal/<int:id>/', views.animal_detail, name="animal_detail"),
    path('racas/', views.RacasView.as_view(), name="racas"),
    # path('racas/', views.racas, name="racas"),
    path('hello/', views.hello_world, name="hello"),
    path('hello/<str:nome>', views.hello_world_nome, name="hello_nome"),
]