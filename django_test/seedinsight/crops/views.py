from django.shortcuts import render
from .models import Seed

# Create your views here.
def get_seed_recommendations(request):
    altitude_zone = request.GET.get('altitude_zone', 'Unknown Altitude')
    seeds = Seed.objects.filter(altitude_zone=altitude_zone)
    return render(request, 'seed_recommendations.html', {'seeds': seeds, 'altitude_zone': altitude_zone})
