from django.shortcuts import render
import requests

def index(request):
    weather_data = {}
    if request.method == "POST":
        city = request.POST.get('city')
        api_key = "3a874a9ca721481a4e5a08508b5a9efe"  # replace with your OpenWeatherMap key
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"


        response = requests.get(url).json()

        # ✅ Check if response is valid
        if response.get("cod") == 200:
            weather_data = {
                "city": city,
                "description": response['weather'][0]['description'],
                "temperature": response['main']['temp'],
                "feels_like": response['main']['feels_like'],
            }
        else:
            # show error message returned from API
            weather_data = {"error": response.get("message", "Something went wrong")}

    return render(request, "weather/index.html", {"weather_data": weather_data})
