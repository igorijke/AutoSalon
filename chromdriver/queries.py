from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from .models import Automobile, Order

def filter_automobiles_by_price(db: Session, min_price: float):
    return db.query(Automobile).filter(Automobile.price > min_price).all()

def aggregate_average_price(db: Session):
    return db.query(func.avg(Automobile.price)).scalar()

def join_automobiles_and_orders(db: Session):
    return db.query(Automobile, Order).join(Order, Automobile.id == Order.automobile_id).all()
