from django.urls import path
from .views import *

urlpatterns=[
    path('top_clubs_spent_most/',ExpenditereClubView.as_view(),name='top_clubs_spent_most'),
    path('transfer-records/',TransfersRecordView.as_view(),name='transfer-records'),
    path('accurate-predictions/',TopAccuratePredictionsView.as_view(),name='accurate_predictions'),
    path('top_clubs_by_income/',IncomeClubView.as_view(),name='top_clubs_by_income')
]