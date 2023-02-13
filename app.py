from flask import Flask, request
from flask_cors import CORS
from weather import *

app = Flask(__name__)
CORS(app)


@app.route("/weather", methods=["POST"])
def process_data():
    # Get the data from the client
    data = request.get_json()
    # Extract the city and state from the data
    city = data["city"]
    state = data["state"]
    # Pass the city and state to the get_weather function
    result = get_weather(city, state)
    # Return the result in JSON format
    return result


if __name__ == "__main__":
    app.run()
