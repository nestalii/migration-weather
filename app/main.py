from app.utils import read_weather_csv, fill_weather
from app.utils.interface import get_weather_by_country_and_date

# df = read_weather_csv("data/weather.csv")
# fill_weather(df)

country = input("Enter the country: ").strip()
date = input("Enter the date (YYYY-MM-DD): ").strip()

result = get_weather_by_country_and_date(country, date)
print(result)