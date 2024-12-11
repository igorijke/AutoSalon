from sqlalchemy.orm import Session
from .models import Automobile, Order

def create_automobile(db: Session, brand: str, model: str, price: float):
    new_auto = Automobile(brand=brand, model=model, price=price)
    db.add(new_auto)
    db.commit()
    db.refresh(new_auto)
    return new_auto

def get_automobiles(db: Session):
    return db.query(Automobile).all()

def create_order(db: Session, automobile_id: int, order_date: str):
    new_order = Order(automobile_id=automobile_id, order_date=order_date)
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return new_order

def get_orders(db: Session):
    return db.query(Order).all()
