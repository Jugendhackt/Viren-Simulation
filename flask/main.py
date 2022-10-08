from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def hello():
    database = sqlite3.connect('sql/database.db')
    return render_template('index.html', x=database.execute('SELECT * FROM users').fetchall())


@app.route('/popup')
def popup():
    render_template("popup.html")

if __name__ == "__main__":
    app.run()
