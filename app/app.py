from flask import Flask,jsonify
from helper.helper import get_summary,load_data


app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"welcome to the app": 'home'})

@app.route("/summary")
def summary():
    data = load_data()
    summary = get_summary(data)
    return jsonify(summary)
    

if __name__ == "__main__":
    app.run( host="0.0.0.0", port=5000, debug=True)

