import requests
from django.shortcuts import render
from .config import API_KEY, API_URL
from .forms import CityNameForm
from .models import Query

# Create your views here.

def search_weather(request):
    form = CityNameForm()
    weather_data = None
    city = None

    if request.method == 'POST':
        form = CityNameForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data["city_name"]
            response = requests.get(API_URL, params={"q": city, "appid": API_KEY, "units": "metric"})

            if response.status_code == 200:
                weather_data = response.json()
                Query.objects.create(city_name=city, weather_details=weather_data)

    return render(request, "index.html", {"form":form, "city": city, "weather_details": weather_data})

def get_query_history(request):
    history = Query.objects.all().order_by("-timestamp")

    return render(request, "query_history.html", {"history": history})