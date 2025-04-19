import requests
import pandas as pd
from datetime import datetime
import time

# API-ключ от Visual Crossing
API_KEY = "SET_YOUR_KEY"  # Замените на ваш ключ

# Список городов
cities = ["London,UK", "New York,USA", "Tokyo,Japan", "Sydney,Australia", "Cape Town,South Africa"]

# Период для марта 2025 года
start_date = "2025-03-01"
end_date = "2025-03-31"

# Базовый URL API
base_url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline"

# Функция для получения данных о погоде
def fetch_weather(city, start, end):
    url = f"{base_url}/{city}/{start}/{end}?unitGroup=metric&key={API_KEY}&contentType=json"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 429:
            print(f"Превышен лимит запросов для {city}. Ожидание перед повторной попыткой...")
            time.sleep(60)  # Ожидание 60 секунд перед повторным запросом
            return fetch_weather(city, start, end)  # Повторный запрос
        else:
            print(f"Ошибка получения данных для {city}: {response.status_code}")
            return None
    except requests.RequestException as e:
        print(f"Ошибка запроса для {city}: {e}")
        return None

if __name__ == "__main__":
    start_time = datetime.now()
    print(f"Начало сбора данных: {start_time}")

    # Сбор данных
    all_data = []
    for city in cities:
        print(f"Получение данных для {city}...")
        data = fetch_weather(city, start_date, end_date)
        if data:
            for day in data["days"]:
                all_data.append({
                    "City": city.split(",")[0],
                    "Date": day["datetime"],
                    "Temperature": day["temp"],
                    "Humidity": day["humidity"],
                    "WindSpeed": day["windspeed"]
                })

    # Преобразование в DataFrame и сохранение в CSV
    if all_data:
        df = pd.DataFrame(all_data)
        df.to_csv("weather_data_march_2025.csv", index=False)
        print("Данные сохранены в weather_data_march_2025.csv")
    else:
        print("Данные не собраны.")

    end_time = datetime.now()
    print(f"Завершение: {end_time}. Время выполнения: {end_time - start_time}")