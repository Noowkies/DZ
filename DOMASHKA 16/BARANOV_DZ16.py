from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, select, text
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
import random

connection_string = "sqlite:///DOMASHKA 16/DOMASHKA16.sqlite"
engine = create_engine(connection_string)

Base = declarative_base()


class Clients(Base):
    __tablename__ = "clients"

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(20))
    orders = relationship("Orders", back_populates="client")

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"{self.name}"


class Orders(Base):
    __tablename__ = "orders"

    id = Column(Integer, autoincrement=True, primary_key=True)
    cost = Column(Integer)
    name = Column(String(20))
    client_id = Column(Integer, ForeignKey("clients.id"))
    client = relationship("Clients", back_populates="orders")

    def __init__(self, cost, name, client_id):
        self.cost = cost
        self.name = name
        self.client_id = client_id

    def __str__(self):
        return f"{self.name} {self.cost}"

    def __repr__(self):
        return f"{self.name} {self.cost}"
    


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()



session.add_all([Clients("Sasha"), Clients("Vasya"), Clients("Liza"), Clients("Dima")])
session.commit()

Products = ["Cheese", "Tomato", "Onion", "Meat", "Garlik", "Pickle", "Lemon"]


orders = []
for i in range(0,10):
    orders.append(Orders(random.randint(100,500), random.choice(Products), random.randint(1,4)))


session.add_all(orders)
session.commit()

clients = session.query(Clients).all()
for client in clients:
    print(f"Client ID: {client.id}, client name: {client.name}")
    for order in client.orders:
        print(f"Order name: {order.name} order price: {order.cost}")

session.close()

connection = engine.connect()

query_1 = connection.execute(
    text(
        "SELECT clients.name AS client_name, orders.name AS order_name, orders.cost AS order_cost FROM clients JOIN orders on clients.id = orders.client_id"
    )
)
for row in query_1.mappings():
    client_name = row["client_name"]
    order_name = row["order_name"]
    order_cost = row["order_cost"]
    print(
        f"Client Name: {client_name}\nOrder name: {order_name}\nOrder prise: {order_cost}"
    )

connection.close()