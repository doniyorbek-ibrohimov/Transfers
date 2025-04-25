from django.shortcuts import render
from django.template.context_processors import request
from django.views import View
from mainAPP.models import *

class IndexView(View):
    def get(self,request):
        return render(request,'index.html')

class CLubView(View):
    def get(self,request):
        country = request.GET.get('country')
        clubs = Club.objects.all()
        if country is not None:
            clubs=clubs.filter(country__name=country)
        context={
            'clubs':clubs
        }
        return render(request,'clubs.html',context)

class LatestTransfersView(View):
    def get(self,request):
        transfers=Transfer.objects.filter(season=Season.objects.last()).order_by('-price')
        print(transfers)
        context={
            'transfers':transfers
        }
        return render(request,'latest-transfers.html',context)

class PlayersView(View):
    def get(self,request):
        players=Player.objects.order_by('-price')
        context={
            'players':players
        }
        return render(request,'players.html',context)

class YPlayersView(View):
    def get(self,request):
        players=Player.objects.filter(age__lte=20).order_by('age')
        context={
            'players':players
        }
        return render(request,'U-20 players.html',context)

class TryoutView(View):
    def get(self,request):
        return render(request,'tryouts.html')

class AboutView(View):
    def get(self,request):
        return render(request,'about.html')


class StatsView(View):
    def get(self,request):
        return render(request,'stats.html')