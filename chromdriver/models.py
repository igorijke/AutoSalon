from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Automobile(Base):
    __tablename__ = 'Automobiles'
    id = Column(Integer, primary_key=True, index=True)  
    brand = Column(String, nullable=False)             
    model = Column(String, nullable=False)             
    price = Column(Float, nullable=False)              


class Order(Base):
    __tablename__ = 'Orders'
    id = Column(Integer, primary_key=True, index=True)         
    automobile_id = Column(Integer, ForeignKey('Automobiles.id'))  
    order_date = Column(Date, nullable=False)                 
