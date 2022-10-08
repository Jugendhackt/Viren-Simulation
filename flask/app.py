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

@app.route("/api/results", methods=["GET", "POST"])
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
        phishing = request.form["phishing"]
        sql = """INSERT INTO users (id, cookies, viren, phishing)
                 VALUES (?, ?, ?, ?)"""
        cursor = cursor.execute(sql, (id, cookies, viren, phishing))
        conn.commit() # pyright: ignore
        return "user with the id {} created".format(id), 201


@app.route("/api/results/<int:id>", methods=["GET", "PUT", "DELETE"])
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
                    phishing=?
                WHERE id=? """

        id = request.form["id"]
        cookies = request.form["cookies"]
        viren = request.form["viren"]
        phishing = request.form["phishing"]
        updated_book = {
            "id": id,
            "cookie": cookies,
            "viren": viren,
            "phishing": phishing,
        }
        conn.execute(sql, (id, cookies, viren, phishing, id)) # pyright: ignore
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
        id = request.form["id"]
        cookies = request.form["cookies"]
        viren = request.form["viren"]
        phishing = request.form["phishing"]
        conn = db_connection()
        cursor = conn.cursor() # pyright: ignore
        sql = """INSERT INTO users (id, cookies, viren, phishing) VALUES (?, ?, ?, ?)"""
        cursor = cursor.execute(sql, (id, cookies, viren, phishing))
        conn.commit() # pyright: ignore
        conn.close() # pyright: ignore
        return jsonify({'status': 'success', 'message': 'Timer wurde erfolgreich beendet und Userdaten wurden gespeichert.', })

@app.route('/api/timer/started', methods=['POST'])
def timer(): # Frontend reports when the timer started
    if request.method == 'POST':
        print('Timer started at ' + str(datetime.datetime.now()))
        id = request.form["id"]
        sql = """ INSERT INTO users (id, cookies, viren, phishing) values (?, ?, ?, ?) """
        conn = db_connection()
        cursor = conn.cursor() # pyright: ignore
        cursor.execute(sql, (id, 0, 0, 0))
        conn.commit() # pyright: ignore
        conn.close() # pyright: ignore
        return 'Timer started at ' + str(datetime.datetime.now())

@app.route('/desktop', methods=['GET'])
def desktop():
    return render_template('Desktop.html')

@app.route('/email.html', methods=['GET'])
def emailhtml():
    return render_template("email.html")

if __name__ == "__main__":
    app.run()