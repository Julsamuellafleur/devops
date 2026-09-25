from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Hello World!</h1>
    <a href="/about">About</a>
    """

@app.route("/about")
def about():
    return """
    <h1>About</h1>
    <a href="https://flask.palletsprojects.com/">
        Flask website
    </a>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)