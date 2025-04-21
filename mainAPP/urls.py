from tkinter.font import names

from django.urls import path
from .views import *
urlpatterns=[
    path('',IndexView.as_view(),name='index'),
    path('clubs/',CLubView.as_view(),name='clubs'),
    path('latest-transfers/',LatestTransfersView.as_view(),name='latest-transfers'),
    path('players/',PlayersView.as_view(),name='players'),
    path('y_players/',YPlayersView.as_view(),name='y_players'),
    path('tryouts/',TryoutView.as_view(),name='tryouts'),
    path('about/',AboutView.as_view(),name='about_us')

]