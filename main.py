# main.py
import requests
import matplotlib.pyplot as plt
import seaborn as sns
import os
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

if API_KEY is None:
    print("Error: API key not found! Check your .env file.")
    exit()

# Function to get weather data
def fetch_weather(city="Mumbai"):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error:", response.status_code, response.text)
        return None

# Function to parse weather data
def parse_weather(data):
    dates = []
    temps = []
    humidity = []
    for entry in data["list"]:
        dates.append(entry["dt_txt"])
        temps.append(entry["main"]["temp"])
        humidity.append(entry["main"]["humidity"])
    return dates, temps, humidity

# Function to visualize data
def visualize_weather(dates, temps, humidity, city):
    plt.figure(figsize=(12,6))
    sns.lineplot(x=dates, y=temps, label="Temperature (°C)", color="red")
    sns.lineplot(x=dates, y=humidity, label="Humidity (%)", color="blue")
    plt.xticks(rotation=45)
    plt.xlabel("Date & Time")
    plt.ylabel("Values")
    plt.title(f"Weather Forecast for {city}")
    plt.legend()
    plt.tight_layout()
    plt.show()

# Main program
if __name__ == "__main__":
    city = input("Enter city name: ")
    data = fetch_weather(city)
    if data:
        dates, temps, humidity = parse_weather(data)
        visualize_weather(dates, temps, humidity, city)
