from flask import Flask, request
import requests

app = Flask(__name__)

עכש
LAT = 32.0853
LON = 34.7818

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        date = request.form.get("date")

        url = f"https://archive-api.open-meteo.com/v1/archive?latitude={LAT}&longitude={LON}&start_date={date}&end_date={date}&daily=temperature_2m_max,temperature_2m_min"

        response = requests.get(url)
        data = response.json()

        try:
            max_temp = data["daily"]["temperature_2m_max"][0]
            min_temp = data["daily"]["temperature_2m_min"][0]

            return f"""
            <h2>Weather for {date}</h2>
            <p>Max: {max_temp}°C</p>
            <p>Min: {min_temp}°C</p>
            <a href="/">Back</a>
            """
        except:
            return "Error fetching data"

    return """
    <h1>Check Weather</h1>
    <form method="POST">
        <label>Enter date (YYYY-MM-DD):</label><br>
        <input type="text" name="date"><br><br>
        <button type="submit">Get Weather</button>
    </form>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)