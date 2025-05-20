from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound
from app.models import Weather, WindMeasurements, SessionLocal

def get_weather_by_country_and_date(country: str, date: str) -> str:
    session: Session = SessionLocal()
    try:
        try:
            weather = session.query(Weather).filter_by(country=country).one()
        except NoResultFound:
            return f"Error: No weather data found for the country '{country}'."

        wind_measurements = session.query(WindMeasurements).filter_by(weather_id=weather.id, last_updated=date).all()
        if not wind_measurements:
            return f"Error: No weather measurements found for the country '{country}' on the date '{date}'."

        formatted_measurements = []
        for measurement in wind_measurements:
            formatted_measurements.append(
                f"Wind Degree: {measurement.wind_degree}, "
                f"Wind Speed (kph): {measurement.wind_kph}, "
                f"Wind Direction: {measurement.wind_direction}, "
                f"Sunrise: {measurement.sunrise}, "
                f"Go Outside: {'Yes' if measurement.go_outside else 'No'}"
            )
        return "\n".join(formatted_measurements)
    except Exception as e:
        return f"An unexpected error occurred: {e}"
    finally:
        session.close()