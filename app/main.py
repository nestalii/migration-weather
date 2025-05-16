from app.utils import read_weather_csv, fill_weather

df = read_weather_csv("data/weather.csv")
fill_weather(df)