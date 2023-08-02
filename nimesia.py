import requests

API_BASE_URL = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"

def get_weather_forecast(date):
    url = f"{API_BASE_URL}&dt={date}"
    response = requests.get(url)
    data = response.json()
    return data

def get_weather():
    date = input("Enter the date and time (Unix timestamp): ")
    weather_data = get_weather_forecast(date)
    temperature = weather_data["main"]["temp"]
    print(f"The temperature on {date} is {temperature}°C")

def get_wind_speed():
    date = input("Enter the date and time (Unix timestamp): ")
    weather_data = get_weather_forecast(date)
    wind_speed = weather_data["wind"]["speed"]
    print(f"The wind speed on {date} is {wind_speed} m/s")

def get_pressure():
    date = input("Enter the date and time (Unix timestamp): ")
    weather_data = get_weather_forecast(date)
    pressure = weather_data["main"]["pressure"]
    print(f"The pressure on {date} is {pressure} hPa")

def main():
    while True:
        print("Choose an option:")
        print("1. Get weather")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")
        
        choice = int(input("Enter your choice: "))

        if choice == 1:
            get_weather()
        elif choice == 2:
            get_wind_speed()
        elif choice == 3:
            get_pressure()
        elif choice == 0:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
