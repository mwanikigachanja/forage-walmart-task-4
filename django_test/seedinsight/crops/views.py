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


import requests
from django.shortcuts import render
from .models import Crop

def recommend_seeds(request):
    location = request.GET.get('location', 'Kitale')  # Default to Kitale
    altitude_zone = get_altitude_zone(location)
    
    # Fetch crops based on the altitude zone
    recommended_crops = Crop.objects.filter(altitude_zone=altitude_zone)
    
    return render(request, 'recommend_seeds.html', {
        'location': location,
        'altitude_zone': altitude_zone,
        'recommended_crops': recommended_crops
    })

def get_altitude_zone(location):
    """ Fetches the altitude zone based on location using a weather API. """
    apiKey = 'e57fe133456b8c6ab739fbc3900619d0'  # Replace with actual API key
    try:
        # Fetch latitude and longitude based on location
        geolocation_response = requests.get(f"https://ipapi.co/{location}/json/")
        geo_data = geolocation_response.json()
        lat, lon = geo_data['latitude'], geo_data['longitude']

        # Fetch elevation based on latitude and longitude
        elevation_response = requests.get(f"https://api.open-meteo.com/v1/elevation?latitude={lat}&longitude={lon}")
        elevation = elevation_response.json()['elevation']
        
        # Determine altitude zone based on elevation
        if elevation < 500:
            return 'Lowland Altitude'
        elif elevation >= 500 and elevation < 1400:
            return 'Dryland Altitude'
        elif elevation >= 1400 and elevation < 1500:
            return 'Medium Altitude'
        elif elevation >= 1500 and elevation < 1800:
            return 'Transitional Altitude'
        elif elevation >= 1800:
            return 'Highland Altitude'
        else:
            return 'Unknown Altitude'
    except Exception as e:
        print(f"Error fetching altitude data: {e}")
        return 'Highland Altitude'  # Default if API fails



def add_crop(request):
    if request.method == 'POST':
        form = CropForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crop_list')  # Redirect to crop list page
    else:
        form = CropForm()

    return render(request, 'add_crop.html', {'form': form})

def crop_list(request):
    crops = Seed.objects.all()
    return render(request, 'crop_list.html', {'crops': crops})