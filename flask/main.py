from flask import Flask, render_template
import sqlite3

app = Flask(__name__)
database = sqlite3.connect('sql/database.db')
database.row_factory = sqlite3.Row
database.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, results TEXT)')

@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/popup')
def popup():
    render_template("popup.html")

if __name__ == "__main__":
    app.run()
