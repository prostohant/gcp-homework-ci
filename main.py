from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/")
def home():
    # Return a JSON object instead of a simple string
    # This simulates a real API response
    return jsonify({
        "service": "homework-api",
        "status": "healthy",
        "version": "v1.0"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)