import json
import joblib
from flask import Flask, request

model = joblib.load("model_iris.joblib")

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World!"

@app.route("/predct", methods=["POST"])
def predict():
    data = request.json
    prediction = model.predict(request_json.get("data"))
    prediction_string = [str(d) for d in prediction]

    response_json = {
        "data": request_json.get("data"),
        "prediction": list(prediction_string)
    }

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)