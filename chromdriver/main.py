from sqlalchemy.orm import Session
from .db import SessionLocal, engine
from .models import Base
from .crud import create_automobile, get_automobiles, create_order, get_orders
from .queries import filter_automobiles_by_price, aggregate_average_price, join_automobiles_and_orders

# Створення таблиць
Base.metadata.create_all(bind=engine)

def menu():
    db: Session = SessionLocal()
    try:
        while True:
            print("\n1. Показати всі авто")
            print("2. Додати авто")
            print("3. Вибрати авто дорожчі за ціну")
            print("4. Порахувати середню ціну авто")
            print("5. Додати замовлення")
            print("6. Показати всі замовлення")
            print("7. Об'єднання таблиць (авто та замовлення)")
            print("0. Вийти")
            choice = input("Виберіть опцію: ")

            if choice == "1":
                autos = get_automobiles(db)
                for auto in autos:
                    print(auto.id, auto.brand, auto.model, auto.price)
            elif choice == "2":
                brand = input("Введіть марку авто: ")
                model = input("Введіть модель авто: ")
                price = float(input("Введіть ціну авто: "))
                create_automobile(db, brand, model, price)
            elif choice == "3":
                min_price = float(input("Введіть мінімальну ціну: "))
                autos = filter_automobiles_by_price(db, min_price)
                for auto in autos:
                    print(auto.id, auto.brand, auto.model, auto.price)
            elif choice == "4":
                avg_price = aggregate_average_price(db)
                print(f"Середня ціна: {avg_price}")
            elif choice == "5":
                auto_id = int(input("Введіть ID автомобіля: "))
                order_date = input("Введіть дату замовлення (YYYY-MM-DD): ")
                create_order(db, auto_id, order_date)
            elif choice == "6":
                orders = get_orders(db)
                for order in orders:
                    print(order.id, order.automobile_id, order.order_date)
            elif choice == "7":
                results = join_automobiles_and_orders(db)
                for auto, order in results:
                    print(auto.brand, auto.model, order.order_date)
            elif choice == "0":
                break
            else:
                print("Невірний вибір, спробуйте ще раз.")
    finally:
        db.close()

if __name__ == "__main__":
    menu()
