from flask import Flask, render_template, request, jsonify
import json
import sqlite3

app = Flask(__name__)


def db_connection():
    conn = None
    try:
        conn = sqlite3.connect("books.sqlite")
    except sqlite3.error as e:
        print(e)
    return conn


@app.route("/getdata")
def getdata():
    return render_template("get_data.html")

@app.route("/putdata")
def putdata():
    return render_template("put_data.html")

@app.route("/users", methods=["GET", "POST"])
def users():
    conn = db_connection()
    cursor = conn.cursor()

    if request.method == "GET":
        cursor = conn.execute("SELECT * FROM users")
        books = [
            dict(id=row[0], result=row[2])
            for row in cursor.fetchall()
        ]
        if books is not None:
            return jsonify(books)

    if request.method == "POST":
        new_id = request.form["id"]
        new_result = request.form["result"]
        sql = """INSERT INTO users (id, results)
                 VALUES (?, ?)"""
        cursor = cursor.execute(sql, (new_id, new_result))
        conn.commit()
        return f"Book with the id: 0 created successfully", 201


@app.route("/book/<int:id>", methods=["GET", "PUT", "DELETE"])
def single_book(id):
    conn = db_connection()
    cursor = conn.cursor()
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
                SET result=?,
                    id=?,
                    result=?
                WHERE id=? """

        new_id = request.form["id"]
        new_result = request.form["result"]
        updated_book = {
            "id": id,
            "result": result,
        }
        conn.execute(sql, (new_id, new_result))
        conn.commit()
        return jsonify(updated_book)

    if request.method == "DELETE":
        sql = """ DELETE FROM book WHERE id=? """
        conn.execute(sql, (id,))
        conn.commit()
        return "The book with id: {} has been ddeleted.".format(id), 200


if __name__ == "__main__":
    app.run(debug=True)