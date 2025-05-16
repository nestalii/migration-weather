from sqlalchemy import Column, Integer, Float, Date, Time, Enum, ForeignKey
from sqlalchemy.orm import relationship
from app.models import Base, WindDirection

class WindMeasurements(Base):
    __tablename__ = "wind_measurements"

    id = Column(Integer, primary_key=True, autoincrement=True)
    weather_id = Column(Integer, ForeignKey("weather.id", ondelete="CASCADE"))
    wind_degree = Column(Integer)
    wind_kph = Column(Float)
    wind_direction = Column(Enum(WindDirection))
    last_updated = Column(Date)
    sunrise = Column(Time)

    weather = relationship("Weather", back_populates="wind_measurements")