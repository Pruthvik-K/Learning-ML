from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/get_location_names')
def get_location_names():
    resopnse = jsonify({
        'locations' : util.get_location_names()
    })
    response.headers.add("Access-Control-Allow-Origin", '*')

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    app.run()
