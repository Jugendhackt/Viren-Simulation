from flask import Flask, render_template, request, jsonify, escape
import json
import sqlite3
import datetime
from ratelimit import limits, RateLimitException
from backoff import on_exception, expo
# from config import *

app = Flask(__name__)


def db_connection():
    conn = None
    try:
        conn = sqlite3.connect("flask/database.db")
    except sqlite3.error as e: # pyright: ignore
        print(e)
    return conn

@on_exception(expo, RateLimitException, max_tries=1)
@limits(calls=10, period=60, ) # 5 calls per minute
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')
    
@app.route('/end', methods=['GET'])
def end():
    return render_template('EndSeite.html')

@limits(calls=5, period=60)
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
        return "user with the id {} created".format(escape(id)), 201

@limits(calls=5, period=60)
@app.route("/api/results/<id>", methods=["GET", "PUT", "DELETE"])
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
                    viren=?,
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
        return "user with the id {} has been  D E S T R O Y E D.".format(escape(id)), 200

@limits(calls=5, period=60)
@app.route('/api/timer/fertig', methods=['POST'])
def fertig():
    if request.method == 'POST':
        id = request.form["id"]
        cookies = request.form["cookies"]
        viren = request.form["viren"]
        phishing = request.form["phishing"]
        conn = db_connection()
        cursor = conn.cursor() # pyright: ignore
        sql = """UPDATE users
                SET id=?,
                    cookies=?,
                    viren=?,
                    phishing=?
                WHERE id=? """
        cursor = cursor.execute(sql, (id, cookies, viren, phishing, id))
        conn.commit() # pyright: ignore
        conn.close() # pyright: ignore
        return jsonify({'status': 'success', 'message': 'Timer wurde erfolgreich beendet und Userdaten wurden gespeichert.', })

@limits(calls=5, period=60)
@app.route('/api/timer/started', methods=['POST'])
def timer(): # Frontend reports when the timer started
    if request.method == 'POST':
        print('Timer started at ' + str(datetime.datetime.now()))
        id = request.json
        sql = """ INSERT INTO users (id, cookies, viren, phishing) values (?, ?, ?, ?) """
        conn = db_connection()
        cursor = conn.cursor() # pyright: ignore
        cursor.execute(sql, (str(id['id']), 0, 0, 0))
        conn.commit() # pyright: ignore
        conn.close() # pyright: ignore
        return 'Timer started at ' + str(datetime.datetime.now())

@limits(calls=5, period=60)
@app.route('/desktop', methods=['GET'])
def desktop():
    return render_template('Desktop.html')

@limits(calls=5, period=60)
@app.route('/getmail/<name>')
def getmail(name):
    if 'css' in name:
        return
    else:
        return render_template(f'{name}/{name}.html')

@limits(calls=5, period=60)
@app.route('/email.html')
def emailget():
    return render_template('email.html')

@app.route('/website', methods=['GET'])
def websiteget():
    return render_template('website.html')

@app.route('/browser', methods=['GET'])
def browserget():
    return render_template('browser.html')

@app.route('/file_manger.html')
def file_manger():
    return render_template('file_manger.html')

if __name__ == "__main__":
    app.run()