from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base
import enum

class WindDirection(enum.Enum):
    N = "N"
    NE = "NE"
    E = "E"
    SE = "SE"
    S = "S"
    SW = "SW"
    W = "W"
    NW = "NW"

class Weather(Base):
    __tablename__ = "weather"

    id = Column(Integer, primary_key=True, autoincrement=True)
    country = Column(String, nullable=False)

    wind_measurements = relationship("WindMeasurements", back_populates="weather", cascade="all, delete")
