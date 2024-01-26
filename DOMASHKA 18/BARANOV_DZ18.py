from flask import Flask, Response

app = Flask(__name__)

a = 0

@app.route("/", methods=["GET"])
def main():
    return str(a)


@app.route("/plus", methods=["POST"])
def plus():
    global a
    a = a + 1
    return Response(status = 200)


@app.route("/minus", methods=["POST"])
def minus():
    global a
    a = a - 1
    return Response(status = 200)


if __name__ == "__main__":
    app.run()