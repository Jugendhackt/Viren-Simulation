from flask import Flask, render_template, request, jsonify
import json
import sqlite3
import datetime

app = Flask(__name__)


def db_connection():
    conn = None
    try:
        conn = sqlite3.connect("flask/database.db")
    except sqlite3.error as e: # pyright: ignore
        print(e)
    return conn

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/getdata")
def getdata():
    return render_template("get_data.html")

@app.route("/putdata")
def putdata():
    return render_template("put_data.html")

@app.route("/results", methods=["GET", "POST"])
def books():
    conn = db_connection()
    cursor = conn.cursor() # pyright: ignore

    if request.method == "GET":
        cursor = conn.execute("SELECT * FROM users ORDER BY id") # pyright: ignore
        results = [
            dict(id=row[0], cookies=row[1], viren=row[2])
            for row in cursor.fetchall()
        ]
        if results is not None:
            return str(results)

    if request.method == "POST": # Diese Methode ist zum erstellen von Daten
        id = request.form["id"]
        cookies = request.form["cookies"]
        viren = request.form["viren"]
        sql = """INSERT INTO users (id, cookies, viren)
                 VALUES (?, ?, ?)"""
        cursor = cursor.execute(sql, (id, cookies, viren))
        conn.commit() # pyright: ignore
        return "user with the id {} created".format(id), 201


@app.route("/results/<int:id>", methods=["GET", "PUT", "DELETE"])
def single_book(id):
    conn = db_connection()
    cursor = conn.cursor() # pyright: ignore
    results = None
    if request.method == "GET":
        cursor.execute("SELECT * FROM users WHERE id=?", (id,))
        rows = cursor.fetchall()
        for r in rows:
            results = r
        if results is not None:
            return jsonify(results), 200
        else:
            return "Something went wrong, this was NOT reported (lol)", 404

    if request.method == "PUT": # Diese methode ist zum updaten der Daten
        sql = """UPDATE users
                SET id=?,
                    cookies=?,
                    viren=?
                WHERE id=? """

        id = request.form["id"]
        cookies = request.form["cookies"]
        viren = request.form["viren"]
        updated_book = {
            "id": id,
            "cookie": cookies,
            "viren": viren,
        }
        conn.execute(sql, (id, cookies, viren, id)) # pyright: ignore
        conn.commit() # pyright: ignore
        return jsonify(updated_book)

    if request.method == "DELETE":
        sql = """ DELETE FROM users WHERE id=? """
        conn.execute(sql, (id,)) # pyright: ignore
        conn.commit() # pyright: ignore 
        return "user with the id {} has been  D E S T R O Y E D.".format(id), 200

@app.route('/api/timer/fertig', methods=['POST'])
def fertig():
    if request.method == 'POST':
        data = request.get_json()
        print(data)
        return jsonify(data)

@app.route('/api/timer/started', methods=['POST'])
def timer(): # Frontend reports when the timer started
    if request.method == 'POST':
        print('Timer started at ' + str(datetime.datetime.now()))
        return 'soon:tm:'

if __name__ == "__main__":
    app.run()