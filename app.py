from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello"

@app.route("/about")
def about():
    return "Tyan"

if __name__ == "__main__":
    app.run(debug=True)