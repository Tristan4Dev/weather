import requests

API_KEY = '90a3b40731cf322babd83c616d28406f'
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def obtenir_meteo_ville(ville):
    url = f"{BASE_URL}?q={ville}&appid={API_KEY}&units=metric&lang=fr"
    
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        ville_nom = data["name"]
        temperature = data["main"]["temp"]
        description = data["weather"][0]["description"]
        print(f"Météo pour {ville_nom}: {temperature}°C, {description}")
    else:
        print("Erreur lors de la récupération des données météorologiques.")

if __name__ == "__main__":

    ville = input("Entrez le nom de la ville : ")
    obtenir_meteo_ville(ville)
