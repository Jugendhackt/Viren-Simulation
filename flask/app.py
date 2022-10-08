from flask import Flask, render_template, request, jsonify
import json
import sqlite3

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

    if request.method == "POST":
        id = request.form["id"]
        cookies = request.form["cookies"]
        viren = request.form["viren"]
        sql = """INSERT INTO users (id, cookies, viren)
                 VALUES (?, ?, ?)"""
        cursor = cursor.execute(sql, (id, cookies, viren))
        conn.commit() # pyright: ignore
        return f"Book with the id: 0 created successfully", 201


@app.route("/book/<int:id>", methods=["GET", "PUT", "DELETE"])
def single_book(id):
    conn = db_connection()
    cursor = conn.cursor() # pyright: ignore
    book = None
    if request.method == "GET":
        cursor.execute("SELECT * FROM book WHERE id=?", (id,))
        rows = cursor.fetchall()
        for r in rows:
            book = r
        if book is not None:
            return jsonify(book), 200
        else:
            return "Something wrong", 404

    if request.method == "PUT":
        sql = """UPDATE book
                SET title=?,
                    author=?,
                    language=?
                WHERE id=? """

        author = request.form["author"]
        language = request.form["language"]
        title = request.form["title"]
        updated_book = {
            "id": id,
            "author": author,
            "language": language,
            "title": title,
        }
        conn.execute(sql, (author, language, title, id)) # pyright: ignore
        conn.commit() # pyright: ignore
        return jsonify(updated_book)

    if request.method == "DELETE":
        sql = """ DELETE FROM book WHERE id=? """
        conn.execute(sql, (id,)) # pyright: ignore
        conn.commit() # pyright: ignore 
        return "The book with id: {} has been ddeleted.".format(id), 200


if __name__ == "__main__":
    app.run()