import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("WEATHER_API_KEY")

def get_weather_data(city):
   
    
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    
    try:
        response = requests.get(url)
        
        if response.status_code == 429:
            print("System Busy: API rate limit reached. Please try again in 60 seconds.")
            return None
        
        response.raise_for_status() 
        
        return response.json()

    except requests.exceptions.RequestException as e:
        print(f"Connection Error: {e}")
        return None

if __name__ == "__main__":
    get_weather_data("London")