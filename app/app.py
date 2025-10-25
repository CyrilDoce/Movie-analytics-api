from flask import Flask,jsonify
from helper.helper import get_summary,load_data


app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"welcome to the app": 'home'})

#READ
@app.route("/summary", methods=['GET'])
def summary():
    data = load_data()
    summary = get_summary(data)
    return jsonify(summary)

#CREATE
@app.route("/insert", methods=['PUT'])     
def insert():
    pass

#DELETE
@app.route("/delete",methods = ['DELETE'])
def delete():
    pass

#UPDATE
@app.route("/update", methods = ['UPDATE'])
def update():
    pass

if __name__ == "__main__":
    app.run( host="0.0.0.0", port=5000, debug=True)

