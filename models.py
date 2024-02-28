from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import  Column, DateTime, Float, Integer, String
from services import engine
from sqlalchemy.orm import sessionmaker
 
Base = declarative_base()

# creating model
class Info(Base):
    __tablename__ = "Info"
 
    id = Column(Integer, primary_key=True, index=True)
    device = Column('device', String) 
    date = Column('date', DateTime) 
    x = Column('x', Float)
    y = Column('y', Float)
    z = Column('z', Float)

SessionLocal = sessionmaker(autoflush=False, bind=engine)
