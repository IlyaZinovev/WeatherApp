from flask import Flask, request
from back import get_struct_data

app = Flask(__name__)


@app.route("/weather")
def get_weather():
    city = request.args.get("city", "")
    days = int(request.args.get("days", ""))
    return get_struct_data(city, days)
