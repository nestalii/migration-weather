import pandas as pd
from sqlalchemy.orm import Session
from app.models import Weather, SessionLocal, WindDirection, WindMeasurements

def read_weather_csv(file_path):
    df = pd.read_csv(file_path)

    df = df[[
        'country',
        'wind_degree',
        'wind_kph',
        'wind_direction',
        'last_updated',
        'sunrise'
    ]]

    return df

def should_go_outside(wind_kph: float) -> bool:
    return wind_kph < 20

def fill_weather(df: pd.DataFrame):
    session: Session = SessionLocal()

    try:
        for _, row in df.iterrows():
            weather = Weather(
                country=row['country']
            )
            session.add(weather)
            session.commit()

            wind_measurement = WindMeasurements(
                weather_id=weather.id,
                wind_degree=int(row['wind_degree']) if not pd.isna(row['wind_degree']) else None,
                wind_kph=float(row['wind_kph']) if not pd.isna(row['wind_kph']) else None,
                wind_direction=WindDirection[row['wind_direction']] if row['wind_direction'] in WindDirection.__members__ else None,
                last_updated=pd.to_datetime(row['last_updated']).date() if not pd.isna(row['last_updated']) else None,
                sunrise=pd.to_datetime(row['sunrise']).time() if not pd.isna(row['sunrise']) else None,
                go_outside = should_go_outside(float(row['wind_kph'])) if not pd.isna(row['wind_kph']) else None
            )
            session.add(wind_measurement)

        session.commit()
    except Exception as e:
        session.rollback()
        print(f"Error occurred: {e}")
    finally:
        session.close()
