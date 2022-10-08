from flask import *

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/popup')
def popup():
    render_template("popup.html")

if __name__ == "__main__":
    app.run()
