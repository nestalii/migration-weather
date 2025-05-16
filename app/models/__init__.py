from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .base import Base
from .weather import Weather, WindDirection
from .wind_measurements import WindMeasurements
from app.utils import DATABASE_URL

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)