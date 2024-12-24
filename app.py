from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

# External API for fun facts (BoredAPI or similar)
FUN_FACT_API_URL = "https://uselessfacts.jsph.pl/random.json?language=en"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get-fact', methods=['GET'])
def get_fact():
    try:
        # Fetch a random fact from the external API
        response = requests.get(FUN_FACT_API_URL)
        if response.status_code == 200:
            data = response.json()
            return jsonify({"fact": data.get("text", "Could not fetch a fun fact!")})
        else:
            return jsonify({"fact": "Failed to fetch a fun fact! Please try again later."})
    except Exception as e:
        return jsonify({"fact": f"An error occurred: {str(e)}"})

if __name__ == '__main__':
    app.run(debug=True)
