import json
from flask import request
from config import app
from models import User, Order, Offer
from service import init_db, get_all, get_all_by_id, insert_data_users, update_universal, insert_data_orders, \
    insert_data_offers, delete_universal


@app.route("/users/", methods=['GET', 'POST'])
def get_users():
    if request.method == 'GET':
        return app.response_class(
            response=json.dumps(get_all(User), indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )
    elif request.method == 'POST':
        if isinstance(request.json, list):
            insert_data_users(request.json)
        elif isinstance(request.json, dict):
            insert_data_users([request.json])
        else:
            print("Непонятный тип данных!")

        return app.response_class(
            response=json.dumps(request.json, indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )


@app.route("/users/<int:user_id>/", methods=["GET", "PUT", "DELETE"])
def get_users_by_id(user_id):
    if request.method == "GET":
        data = get_all_by_id(User, user_id)
        return app.response_class(
            response=json.dumps(data, indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )
    elif request.method == "PUT":
        update_universal(User, user_id, request.json)
        return app.response_class(
            response=json.dumps(["OK"], indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )
    elif request.method == "DELETE":
        delete_universal(User, user_id)
        return app.response_class(
            response=json.dumps(["OK"], indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )


@app.route("/orders/", methods=["GET", "POST"])
def get_orders():
    if request.method == "GET":
        return app.response_class(
            response=json.dumps(get_all(Order), indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )
            #result = json.dumps(get_all(Order), indent=4, ensure_ascii=False)
            #return jsonify(result)
    elif request.method == "POST":
        if isinstance(request.json, list):
            insert_data_orders(request.json)
        elif isinstance(request.json, dict):
            insert_data_orders([request.json])
        else:
            print("Непонятный тип данных!")

        return app.response_class(
            response=json.dumps(request.json, indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )


@app.route("/orders/<int:user_id>/", methods=["GET", "PUT", "DELETE"])
def get_orders_by_id(user_id):
    if request.method == "GET":
        data = get_all_by_id(Order, user_id)
        return app.response_class(
            response=json.dumps(data, indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )
    elif request.method == "PUT":
        update_universal(Order, user_id, request.json)
        return app.response_class(
            response=json.dumps(["OK"], indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )
    elif request.method == "DELETE":
        delete_universal(Order, user_id)
        return app.response_class(
            response=json.dumps(["OK"], indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )


@app.route("/offers/", methods=["GET", "POST"])
def get_offers():
    if request.method == "GET":
        return app.response_class(
            response=json.dumps(get_all(Offer), indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )
    elif request.method == "POST":
        if isinstance(request.json, list):
            insert_data_offers(request.json)
        elif isinstance(request.json, dict):
            insert_data_offers([request.json])
        else:
            print("Непонятный тип данных!")

        return app.response_class(
            response=json.dumps(request.json, indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )


@app.route("/offers/<int:user_id>/", methods=["GET", "PUT", "DELETE"])
def get_offers_by_id(user_id):
    if request.method == "GET":
        data = get_all_by_id(Offer, user_id)
        return app.response_class(
            response=json.dumps(data, indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )
    elif request.method == "PUT":
        update_universal(Offer, user_id, request.json)
        return app.response_class(
            response=json.dumps(["OK"], indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )
    elif request.method == "DELETE":
        delete_universal(Offer, user_id)
        return app.response_class(
            response=json.dumps(["OK"], indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )


if __name__ == '__main__':
    init_db()
    app.run(host="0.0.0.0", port=8080, debug=True)
