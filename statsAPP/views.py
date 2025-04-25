from django.shortcuts import render
from mainAPP.models import *
from django.views import View
from django.db.models import Sum, Q, ExpressionWrapper, FloatField,F
from django.db.models.functions import Abs


class ExpenditereClubView(View):
    def get(self, request):
        clubs = Club.objects.annotate(
            total_spent=Sum('new_club__price', filter=Q(new_club__season=Season.objects.last()))
        ).filter(total_spent__gt=0).order_by('-total_spent')[:50]

        context = {
            'clubs': clubs
        }
        return render(request, 'stats/top-50-clubs-by-expenditure.html', context)

class TransfersRecordView(View):
    def get(self,request):
        transfers=Transfer.objects.order_by('-price')
        context={
            'transfers':transfers
        }
        return render(request,'stats/transfer-records.html',context)

class TopAccuratePredictionsView(View):
    def get(self,request):
        accurate_transfers = Transfer.objects.annotate(
            percent_diff=ExpressionWrapper(
                Abs(F('price') - F('price_tft')) / F('price') * 100,
                output_field=FloatField()
            )
        ).order_by('percent_diff')
        context={
            'transfers':accurate_transfers
        }
        return render(request,'stats/150-accurate-predictions.html',context)

class IncomeClubView(View):
    def get(self, request):
        clubs = Club.objects.annotate(
            total_income=Sum('old_club__price', filter=Q(old_club__season=Season.objects.last()))
        ).filter(total_income__gt=0).order_by('-total_income')[:50]

        context = {
            'clubs': clubs
        }
        return render(request, 'stats/top-50-clubs-by-income.html', context)
