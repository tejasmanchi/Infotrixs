import time
import pyfiglet
from simple_chalk import chalk
import requests

# API key of https://openweathermap.org/
apikey = "db16727ad9f8af2632dce08f5a0870c0"

# Base URL for the API
baseurl = "https://api.openweathermap.org/data/2.5/weather"

weathericons = {
    # day icons
    "01d": "☀️",
    "02d": "⛅️",
    "03d": "☁️",
    "04d": "☁️",
    "09d": "🌧",
    "10d": "🌦",
    "11d": "⛈",
    "13d": "🌨",
    "50d": "🌫",
    # night icons
    "01n": "🌙",
    "02n": "☁️",
    "03n": "☁️",
    "04n": "☁️",
    "09n": "🌧",
    "10n": "🌦",
    "11n": "⛈",
    "13n": "🌨",
    "50n": "🌫",
}

favorite_cities = []  # List to store favorite cities

def fetch_weather(city):
        url = f"{baseurl}?q={city}&appid={apikey}&units=metric" # put all the parameter and value pairs after '?'   
        response = requests.get(url)
        if response.status_code == 200: # status code of 200 means that the request was successful, and the server has returned the expected data
            data = response.json()
            temperature = data["main"]["temp"]
            feelslike = data["main"]["feels_like"]
            description = data["weather"][0]["description"]
            icon = data["weather"][0]["icon"]
            city_name = data["name"]
            weathericon = weathericons.get(icon, "")
            output = f"{pyfiglet.figlet_format(city_name)}\n\n"
            output += f"{weathericon} {description}\n"
            output += f"Temp =  {temperature}C\n"
            output += f"Feels Like =  {feelslike}C\n"
            print(chalk.green(output))
        else:
            print(f'Failed to fetch weather data for {city}')
            print(f'Error message: {response.text}')

def add_favorite(city):
    if city not in favorite_cities:
        favorite_cities.append(city)
        print(f"{city} added to favorites.")
    else:
        print(f"{city} is already in your favorites.")

def remove_favorite(city):
    if city in favorite_cities:
        favorite_cities.remove(city)
        print(f"{city} removed from favorites.")
    else:
        print(f"{city} is not in your favorites.")

def list_favorites():
    print("Favorite Cities:")
    for city in favorite_cities:
        print(city)

def main():
    while True:
        print("\nOptions:")
        print("1. Check Weather")
        print("2. Add to Favorites")
        print("3. Remove from Favorites")
        print("4. List Favorites")
        print("5. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            city = input("Enter the city name to check weather: ")
            while True:
                fetch_weather(city)
                time.sleep(5)
                option = input("Press Enter to refresh, or type 'b' to go back: ")
                if option == "b":
                    break             
        elif choice == "2":
            city = input("Enter the city name to add to favorites: ")
            add_favorite(city)
        elif choice == "3":
            city = input("Enter the city name to remove from favorites: ")
            remove_favorite(city)
        elif choice == "4":
            list_favorites()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
