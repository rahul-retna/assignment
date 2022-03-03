from flask import Flask, send_from_directory, redirect, request, jsonify
from utils.parse_data import parse
from utils.prediction import predict_charge

app = Flask(__name__)

@app.route('/')
def home():
    return redirect("/static/index.html")

@app.route('/predict', methods=['POST'])
def predict():
    age = parse(request, "age")
    sex = parse(request, "sex")
    bmi = parse(request, "bmi")
    children = parse(request, "children")
    smoker = parse(request, "smoker")
    region = parse(request, "region")

    charge = predict_charge(age, sex, bmi, children, smoker, region)
    status = charge is not None
    result = {
        "success": status
    }

    if status:
        result["charge"] = charge
    return jsonify(result)

@app.route('/static/<path:path>')
def static_files(path):
    return send_from_directory("./static/", path)


# start app
if __name__ == '__main__':
    app.run(debug=True)
