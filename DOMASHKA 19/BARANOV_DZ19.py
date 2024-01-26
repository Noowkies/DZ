from sqlalchemy import create_engine, text
from flask import Flask, render_template

connection_string = "sqlite:///DOMASHKA 16/DOMASHKA16.sqlite"
engine = create_engine(connection_string)

class Orders():

    def __init__(self, cost, name, client_id, id):
        self.id = id
        self.cost = cost
        self.name = name
        self.client_id = client_id

app = Flask(__name__)

orders = []

@app.route("/", methods=["GET"])
def main():
    global orders
    return render_template("index.html", data = orders) 


def initDB():
    connection = engine.connect()
    query_1 = connection.execute(
        text(
            "SELECT * FROM orders"
        )
    )
    for row in query_1.mappings():
        client_id = row["client_id"]
        id = row["id"]
        name = row["name"]
        cost = row["cost"]
        global orders
        print(f"id: {id}, name: {name}, cost: {cost}, client_id: {client_id}")
        orders.append(Orders(cost, name, client_id, id))
        

    connection.close()

if __name__ == "__main__":
    initDB()
    app.run()