from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = '90a3b40731cf322babd83c616d28406f'
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def getCityWeather(city):
    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric&lang=fr"
    
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        
        if data["cod"] == "404":
            return None 
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

@app.route("/", methods=["GET", "POST"])
def index():
    weather = None

    if request.method == "POST":
        city = request.form.get("city")
        weather = getCityWeather(city)

    return render_template("index.html", weather=weather)

if __name__ == "__main__":
    app.run(debug=True)
