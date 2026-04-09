import requests
from dotenv import load_dotenv
import os

load_dotenv(".env", override=True)  # Load environment variables from .env file

OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")

class OpenWeatherMap:
    # Class Attribute: The base URL for the API
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

    def __init__(self, api_key, units="metric"):
        # Instance Attributes: Unique to each 'client' object
        self.api_key = api_key
        self.units = units

    # --- Instance Method ---
    def get_weather(self, city):
        """Fetches current weather for a specific city."""
        params = {
            "q": city,
            "appid": self.api_key,
            "units": self.units
        }
        response = requests.get(self.BASE_URL, params=params, timeout=30)  # Added timeout for better error handling
       
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"City {city} not found or API issue."}

    # --- Static Method ---
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        """Utility method: doesn't need 'self' or 'cls'."""
        return (celsius * 9/5) + 32
    
if __name__ == "__main__":
    ### How to use it:
    city = input("Enter city name to get weather: ")
    # 1. Standard initialization (Instance)
    weather_client = OpenWeatherMap(api_key=OPENWEATHER_API_KEY)
    data = weather_client.get_weather(city)
    print(data)
    # print(f"Current temperature in {city}: {data['main']['temp']}°C")

    # 2. Using the Utility (Static)
    temp_c = float(input("Enter temperature in Celsius: "))
    temp_f = OpenWeatherMap.celsius_to_fahrenheit(temp_c)
    print(f"{temp_c}°C is {temp_f}°F")