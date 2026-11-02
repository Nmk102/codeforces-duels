from flask import Flask, render_template, request, jsonify
from cf import is_solved
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/check")
def check():
    handle = request.args.get("handle")
    if not handle:
        return jsonify({"error": "handle is required"}), 400
    solved = is_solved(handle, 1, "A")
    return jsonify({"handle": handle, "solved": solved})

if __name__ == "__main__":
    app.run(debug=True)