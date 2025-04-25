from .models import *
from django.db.models import Count

def get_countries(request):
    countries=Country.objects.annotate(clubs_count=Count('club')).filter(clubs_count__gt=0).order_by('-clubs_count')
    l=countries.count()
    if l%2==0:
        left_countries=countries[:l//2]
        right_countries=countries[l//2:]
    else:
        left_countries = countries[:l // 2 +1]
        right_countries = countries[l // 2 +1:]
    context={
        'left_countries':left_countries,
        'right_countries':right_countries,
    }

    return context