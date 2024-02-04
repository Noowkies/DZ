from flask import Flask, g, render_template, request, make_response
from db.database import get_orders,  get_order_by_id , delete_order, update_order


app = Flask(__name__)


@app.route("/", methods=["GET"])
def main():
    orders = get_orders()
    return render_template("index.html", data = orders) 

@app.route("/orders/update", methods=["GET", "POST"])
def update():
    if request.method == "POST":
         id = request.form["id"]
         name = request.form["name"]
         cost = request.form["cost"]
         update_order(id, cost, name)
         return make_response("Updated!", 201)
    id = request.args.get("id")
    if not id:
            return make_response("id not found!", 400)
    order = get_order_by_id(id)
    print(id)
    return render_template("update.html", data = order) 

@app.route("/orders/delete", methods=["POST"])
def delete():
    id = request.form["id"]
    if not id:
            return make_response("id not found!", 400)
    delete_order(id)
    return make_response("Deleted", 201)

if __name__ == "__main__":
    app.run()