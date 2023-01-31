from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/test")
def test():
    return "<p>test route page!</p>"


@app.route("/home")
def home():
    return "<p>test home page!</p>"

@app.route("/admin")
def admin():
    return "<p>test admin page!</p>"

if __name__ == "__main__":
    app.run()
