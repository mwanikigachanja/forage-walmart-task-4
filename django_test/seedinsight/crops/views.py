import requests
from django.shortcuts import render
from .models import Crop

# Homepage view
def homepage(request):
    return render(request, 'homepage.html')

# Seed recommendation view
def recommend_seeds(request):
    location = request.GET.get('location', 'Kitale')  # Default location is Kitale
    altitude_zone, weather_data = get_altitude_zone(location)  # Fetch altitude zone and weather info
    
    recommended_crops = Crop.objects.filter(altitude_zone=altitude_zone)  # Get crops for the altitude zone
    
    return render(request, 'recommend_seeds.html', {
        'location': location,
        'altitude_zone': altitude_zone,
        'recommended_crops': recommended_crops,
        'weather_data': weather_data  # Pass weather data to template
    })

# Helper function to get the altitude zone and weather data
def get_altitude_zone(location):
    apiKey = 'e57fe133456b8c6ab739fbc3900619d0'  # Replace with your OpenWeather API key
    
    try:
        # Fetch weather and location data from OpenWeather API
        weather_response = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={apiKey}&units=metric"
        )
        weather_data = weather_response.json()
        
        # Get latitude and longitude from the OpenWeather API response
        lat, lon = weather_data['coord']['lat'], weather_data['coord']['lon']
        
        # Fetch elevation data based on latitude and longitude using Open-Meteo API
        elevation_response = requests.get(f"https://api.open-meteo.com/v1/elevation?latitude={lat}&longitude={lon}")
        elevation = elevation_response.json()['elevation']
        
        # Determine the altitude zone based on elevation
        if elevation < 500:
            altitude_zone = 'Lowland Altitude'
        elif elevation >= 500 and elevation < 1400:
            altitude_zone = 'Dryland Altitude'
        elif elevation >= 1400 and elevation < 1500:
            altitude_zone = 'Medium Altitude'
        elif elevation >= 1500 and elevation < 1800:
            altitude_zone = 'Transitional Altitude'
        elif elevation >= 1800 and elevation < 2800:
            altitude_zone = 'Highland Altitude'
        else:
            altitude_zone = 'Unknown Altitude'
        
        # Return the altitude zone and weather data for display
        return altitude_zone, {
            'temperature': weather_data['main']['temp'],
            'description': weather_data['weather'][0]['description'],
            'humidity': weather_data['main']['humidity'],
            'wind_speed': weather_data['wind']['speed'],
            'cloudiness': weather_data['clouds']['all']
        }
    
    except Exception as e:
        # Fallback to default altitude zone if any API call fails
        return 'Highland Altitude', {}

