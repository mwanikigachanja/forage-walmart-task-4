"""
URL configuration for seedinsight project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from crops.views import get_seed_recommendations, home # Import the function
from crops.views import add_crop  # Import the add_crop view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('recommendations/', get_seed_recommendations, name='seed_recommendations'),
    path('', home, name='home'),  # Add the root URL pattern
     path('admin/add-crop/', add_crop, name='add_crop'),  # Add the URL pattern for the add crop page
]
