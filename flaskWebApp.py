from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

# Read cars.csv into a pandas dataframe
DATA = pd.read_csv("cars.csv")

# Convert the df to a list of dictionaries so Flask can send it as JSON
CARS = DATA.to_dict(orient="records")

@app.get("/hello")
def hello():
    return jsonify({
        "message": "Hello! Welcome to my First API!",
        "routes": ["/api/health", "/data", "/data/1", "/data/first10"]
    }), 200

@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({"status": "OK"}), 200

@app.route("/data", methods=["GET", "POST"])
def data():
    if request.method == "GET":
        return jsonify(CARS)

    elif request.method == "POST":
        # Read the JSON the client sent
        new_data = request.get_json()
        if not new_data:
            return jsonify({"error": "Request body must be JSON"}), 400

        # Require at least a name and a price
        if "CarName" not in new_data or "price" not in new_data:
            return jsonify({"error": "JSON must include 'CarName' and 'price'"}), 400

        # Give it the next ID
        new_data["car_ID"] = max(car["car_ID"] for car in CARS) + 1

        # Add it to the list (in memory, so it resets when the server restarts).
        CARS.append(new_data)

        return jsonify({"message": "Car added", "car": new_data}), 201


@app.route('/data/<int:item_id>', methods=['GET'])
def get_item(item_id):
    for car in CARS:
        if car["car_ID"] == item_id:
            return jsonify(car), 200

    return jsonify({"error": "Car not found"}), 404

# Gets first 10 rows
@app.route("/data/first10", methods=["GET"])
def first_ten():
    first_rows = DATA.head(10).to_dict(orient="records")
    return jsonify(first_rows), 200


if __name__ == '__main__':
    app.run(debug=True,port=5000)
