from flask import Flask, request

app = Flask(__name__)

@app.route('/add', methods=['GET'])
def add():

    data = request.json
    a = float(data['a'])
    b = float(data['b'])
    return str(a + b)

if __name__ == "__main__":
    app.run()