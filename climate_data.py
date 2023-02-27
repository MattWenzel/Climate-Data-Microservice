from flask import Flask, request
from flask_cors import CORS
import pandas as pd
import json
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


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


def get_weather(city, state):
    """Web scrapes climate data for a given city from Wikipedia"""
    city = convert_to_snake_case(city)
    state = convert_to_snake_case(state)
    if city is False or state is False:
        return "invalid input"
    try:
        dataframe = get_table(f"https://en.wikipedia.org/wiki/{city},_{state}#Climate")
        if dataframe is None:
            dataframe = get_table(f"https://en.wikipedia.org/wiki/Template:{city}_weatherbox")
            if dataframe is None:
                return f"Error: Climate Data for {city} Not Found"
    except Exception as e:
        return f"{e}"
    dataframe = df_to_json(dataframe)
    return dataframe


def get_table(url):
    """Sorts through the wiki html tables to find the climate data table"""
    html = pd.read_html(url, header=0)
    for table in html:
        row, col, = table.shape
        if row > 2:
            table.columns = table.iloc[0]
            table = table.drop(table.index[0])
            first_word = table.columns[0]
            if first_word == "Month":
                return table.drop(table.index[-2:])
    return None


def df_to_json(dataframe):
    """convert weather dataframe to JSON format"""
    json_dict = {}
    data_list = dataframe.values
    months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec","Year"]
    for stat in data_list:
        json_dict[stat[0]] = {}
        for i in range(0, len(months)):
            json_dict[stat[0]][months[i]] = stat[i+1]
    return json.dumps(json_dict, ensure_ascii=False, indent=4)


def convert_to_snake_case(string):
    """converts string input to snake case for use in Wiki URL"""
    if not isinstance(string, str):
        return False
    words = string.strip().split()
    if not all(word.isalpha() for word in words):
        return False
    return '_'.join([word.capitalize() for word in words])


if __name__ == "__main__":
    app.run()
