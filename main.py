import requests
import json

api_key = "06c7f27d6f6881deb35fbe0cdb5a578e" #from OpenWeatherMap
location = "Melbourne"

url = f"https://api.openweathermap.org/data/2.5/weather?lat=-37.8141705&lon=144.9655616&appid=06c7f27d6f6881deb35fbe0cdb5a578e" #from OpenWeatherMap

#{"coord":{"lon":144.9656,"lat":-37.8142},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01d"}],"base":"stations","main":{"temp":302.08,"feels_like":301.29,"temp_min":297.4,"temp_max":307.98,"pressure":1007,"humidity":35},"visibility":10000,"wind":{"speed":7.2,"deg":180},"clouds":{"all":0},"dt":1674886756,"sys":{"type":2,"id":2008489,"country":"AU","sunrise":1674847706,"sunset":1674898631},"timezone":39600,"id":2158177,"name":"Melbourne","cod":200}


response = requests.get(url)

if response.status_code == 200:  #HTTP status code 200 means response successful 
    weather_stats = json.loads(response.text)

    temperature = weather_stats["main"]["temp"] - 273.15 
    #-273.15 to convert from Kelvin to Celcius 
    feels_like = weather_stats["main"]["feels_like"] - 273.15
    temp_max = weather_stats["main"]["temp_max"] - 273.15
    temp_min = weather_stats["main"]["temp_min"] - 273.15
    humidity = weather_stats["main"]["humidity"]
    description = weather_stats["weather"][0]["description"].capitalize()
# we're using [0] because the list "weather" contains only one element. "Weather" is a dictionary with 4 key-value pairs "id", "main", "description", and "icon", each accesed on index 0. Note: The elements in a list are usually separated by commas and are enclosed in square brackets [].

    print(f"Temperature: {temperature:.1f}°C") #.1f makes result one decimal place 
    print(f"Feels Like: {feels_like:.1f}°C")
    print(f"Temp Max: {temp_max:.1f}°C")
    print(f"Temp Min: {temp_min:.1f}°C")
    print(f"Humidity: {humidity}%")
    print(f"Weather: {description}")
else:
    print("Error: Could not get weather data.")


