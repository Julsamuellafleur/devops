from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>This another string!</h1>
    <a href="/about">About</a><br>
    <a href="/contact">Contact</a>
    """
@app.route("/about")
def about():
    return """
    <h1>About</h1>
    <a href="https://flask.palletsprojects.com/">
        Flask website
    </a>
    """
@app.route("/contact")
def contact():
    return """
    <h1>Contact</h1>
    <p>Email: "C24709519@mytudublin.ie" </p>
    <a href="/">Home</a>
    """    
     


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)