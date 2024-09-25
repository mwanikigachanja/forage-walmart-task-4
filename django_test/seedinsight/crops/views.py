import requests
from django.shortcuts import render
from .models import Crop

def recommend_seeds(request):
    location = request.GET.get('location', 'Kitale')  # Default location is Kitale
    altitude_zone = get_altitude_zone(location)
    
    recommended_crops = Crop.objects.filter(altitude_zone=altitude_zone)
    
    return render(request, 'recommend_seeds.html', {
        'location': location,
        'altitude_zone': altitude_zone,
        'recommended_crops': recommended_crops,
    })

def get_altitude_zone(location):
    apiKey = 'your_weather_api_key'
    
    try:
        # Fetch latitude and longitude using the location name
        geolocation_response = requests.get(f"https://ipapi.co/{location}/json/")
        geo_data = geolocation_response.json()
        lat, lon = geo_data['latitude'], geo_data['longitude']

        # Fetch elevation data based on latitude and longitude
        elevation_response = requests.get(f"https://api.open-meteo.com/v1/elevation?latitude={lat}&longitude={lon}")
        elevation = elevation_response.json()['elevation']
        
        # Determine the altitude zone
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
        return 'Highland Altitude'
