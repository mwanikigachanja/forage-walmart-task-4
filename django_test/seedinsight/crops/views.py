from django.shortcuts import render, redirect
import requests
from crops.models import Seed
from .forms import CropForm

# Create your views here.
def get_seed_recommendations(request):
    altitude_zone = request.GET.get('altitude_zone', 'Unknown Altitude')
    seeds = Seed.objects.filter(altitude_zone=altitude_zone)
    return render(request, 'seed_recommendations.html', {'seeds': seeds, 'altitude_zone': altitude_zone})


def home(request):
    return render(request, 'recommendation.html')  # Render the landing page template


def fetch_location():
    response = requests.get('https://ipapi.co/json/')
    location_data = response.json()
    return location_data['city']

def fetch_weather(location):
    api_key = 'your_openweathermap_api_key'
    weather_url = f'https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric'
    weather_data = requests.get(weather_url).json()

    lat = weather_data['coord']['lat']
    lon = weather_data['coord']['lon']

    altitude_response = requests.get(f'https://api.open-meteo.com/v1/elevation?latitude={lat}&longitude={lon}')
    altitude_data = altitude_response.json()
    elevation = altitude_data['elevation']

    # Determine altitude zone based on elevation
    if elevation < 500:
        altitude_zone = 'Lowland Altitude'
    elif elevation < 1400:
        altitude_zone = 'Dryland Altitude'
    elif elevation < 1500:
        altitude_zone = 'Medium Altitude'
    elif elevation < 1800:
        altitude_zone = 'Transitional Altitude'
    elif elevation < 2800:
        altitude_zone = 'Highland Altitude'
    else:
        altitude_zone = 'Very High Altitude'
    
    return weather_data, altitude_zone


def add_crop(request):
    if request.method == 'POST':
        form = CropForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crop_list')  # Redirect to crop list page
    else:
        form = CropForm()

    return render(request, 'add_crop.html', {'form': form})