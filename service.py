import json
from models import *
from config import db


def insert_data_users(input_data):
    #наполняем User
    for row in input_data:
        db.session.add(
            User(
                id=row.get("id"),
                first_name=row.get("first_name"),
                last_name=row.get("last_name"),
                age=row.get("age"),
                email=row.get("email"),
                role=row.get("role"),
                phone=row.get("phone")
                # **row
            )
        )
    db.session.commit()


def insert_data_orders(input_data):
    # наполняем Order
    for row in input_data:
        db.session.add(
            Order(
                id=row.get("id"),
                name=row.get("name"),
                description=row.get("description"),
                start_date=row.get("start_date"),
                end_date=row.get("end_date"),
                address=row.get("address"),
                price=row.get("price"),
                customer_id=row.get("customer_id"),
                executor_id=row.get("executor_id")
                # **row
            )
        )
    db.session.commit()


def insert_data_offers(input_data):
    # наполняем Offer
    for row in input_data:
        db.session.add(
            Offer(
                id=row.get("id"),
                order_id=row.get("order_id"),
                executor_id=row.get("executor_id")
                # **row
            )
        )
    db.session.commit()


def get_all(model):
    #получаем данные из выбранной модели
    result = []
    for row in db.session.query(model).all():
        result.append(row.to_dict())
    return result


def get_all_by_id(model, user_id):
    # получаем данные из выбранной модели по user_id
    try:
        return db.session.query(model).get(user_id).to_dict()
    except Exception:
        return {}


def update_universal(model, user_id, values):
    #Обновляем данные из базы
    try:
        db.session.query(model).filter(model.id == user_id).update(values)
        db.session.commit()
    except Exception as e:
        print(e)
        return {}


def delete_universal(model, user_id):
    #Удаляем данные из базы
    try:
        db.session.query(model).filter(model.id == user_id).delete()
        db.session.commit()
    except Exception as e:
        print(e)
        return {}


def init_db():
    #при старте очищаем данные, создаем модели и наполняем модели данными
    db.drop_all()
    db.create_all()

    with open("data/users.json", encoding="utf-8") as file:
        data = json.load(file)
        insert_data_users(data)

    with open("data/offers.json", encoding="utf-8") as file:
        data = json.load(file)
        insert_data_offers(data)

    with open("data/orders.json", encoding="utf-8") as file:
        data = json.load(file)
        insert_data_orders(data)
