from sqlalchemy import create_engine, text
from sqlalchemy.orm import declarative_base

Base = declarative_base()

connection_string = "sqlite:///DOMASHKA 20/db/orders.sqlite"
engine = create_engine(connection_string)

class Orders():

    def __init__(self, cost, name, id):
        self.id = id
        self.cost = cost
        self.name = name


def get_orders():
    connection = engine.connect()
    all_orders = connection.execute(
        text(
            "SELECT * FROM orders"
        )
    )
    orders = []
    for row in all_orders.mappings():
        id = row["id"]
        name = row["name"]
        cost = row["cost"]
        orders.append(Orders(cost, name, id))
    connection.close()
    return orders

def get_order_by_id(id):
    connection = engine.connect()
    all_id = connection.execute(
        text(
            f"SELECT * FROM orders WHERE id={id}"
        )
    )
    id_orders = all_id.fetchone()
    id,cost,name = (id_orders[0], id_orders[1], id_orders[2])
    connection.close()
    return Orders(cost, name, id)

def update_order(id,cost,name):
    connection = engine.connect()
    all_id = connection.execute(
        text(
            f"UPDATE orders SET cost = {cost}, name = '{name}' WHERE id= {id}"
        )
    )
    connection.commit()   
    connection.close()

def delete_order(id):
    connection = engine.connect()
    all_id = connection.execute(
        text(
            f"DELETE FROM orders WHERE id={id}"
        )
    )
    connection.commit()
    connection.close()