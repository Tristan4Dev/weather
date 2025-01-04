import requests

API_KEY = '90a3b40731cf322babd83c616d28406f'
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def getCityWeather(city):
    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric&lang=fr"
    
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        
        if data["cod"] == "404":
            return None  # Si la ville n'est pas trouvée
        else:
            city_name = data["name"]
            temperature = round(data["main"]["temp"], 1)
            temperature_max = round(data["main"]["temp_max"], 1)
            temperature_min = round(data["main"]["temp_min"], 1)
            description = data["weather"][0]["description"]
            humidity = data["main"]["humidity"]
            wind_speed = round(data["wind"]["speed"], 1)

            return {
                "city_name": city_name,
                "temperature": temperature,
                "temperature_max": temperature_max,
                "temperature_min": temperature_min,
                "description": description,
                "humidity": humidity,
                "wind_speed": wind_speed
            }
    else:
        return None

def main():
    city = input("Entrez le nom de la ville: ")
    weather = getCityWeather(city)

    if weather:
        print(f"\nMétéo pour {weather['city_name']} :")
        print(f"Température actuelle: {weather['temperature']}°C")
        print(f"Température maximale: {weather['temperature_max']}°C")
        print(f"Température minimale: {weather['temperature_min']}°C")
        print(f"Description: {weather['description']}")
        print(f"Humidité: {weather['humidity']}%")
        print(f"Vitesse du vent: {weather['wind_speed']} m/s")
    else:
        print("Ville non trouvée. Veuillez vérifier le nom de la ville.")

if __name__ == "__main__":
    main()
