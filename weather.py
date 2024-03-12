import requests

def get_weather_data(location):
    api_key = "your_api_key"  # Replace with your actual API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data

def display_current_weather(data):
    if data["cod"] == 200:
        print(f"Current weather in {data['name']}:")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Wind Speed: {data['wind']['speed']} m/s")
    else:
        print("Error fetching weather data. Please try again.")

def display_forecast(location):
    api_key = "your_api_key"  # Replace with your actual API key
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={location}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()

    if data["cod"] == "200":
        print(f"Weather forecast for {data['city']['name']}:")
        for forecast in data["list"]:
            print(f"Date: {forecast['dt_txt']}, Temperature: {forecast['main']['temp']}°C")
    else:
        print("Error fetching forecast data. Please try again.")

def main():
    print("Welcome to the Weather Forecast Application!")
    location = input("Enter location (city name): ")

    current_weather_data = get_weather_data(location)
    display_current_weather(current_weather_data)

    forecast_option = input("Do you want to see the forecast for the next few days? (yes/no): ")
    if forecast_option.lower() == "yes":
        display_forecast(location)
    else:
        print("Thank you for using the Weather Forecast Application!")

if __name__ == "__main__":
    main()
