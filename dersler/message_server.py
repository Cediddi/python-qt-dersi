import os

from bottle import run, route, request
import sqlite3

db_filename = 'todo.db'

db_is_new = not os.path.exists(db_filename)


def prep():
    with sqlite3.connect(db_filename) as conn:
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE messages (id integer primary key autoincrement not null , sender varchar(50) not null , message text not null);
        """)


@route("/", method="POST")
def send_msg():
    data = request.json
    try:
        with sqlite3.connect(db_filename) as conn:
            cursor = conn.cursor()
            cursor.execute("insert into messages (sender, message) values (?, ?)", (data["sender"], data["message"]))
        return {"status": "OK"}
    except Exception as e:
        return {"status": "FAIL"}, 500


@route("/")
def list_msg():
    with sqlite3.connect(db_filename) as conn:
        cursor = conn.cursor()
        result = cursor.execute("select sender, message from messages order by id")
    data = []
    for r in result:
        data.append({"sender": r[0], "message": r[1]})
    return {"messages": data}


if __name__ == '__main__':
    if db_is_new:
        prep()
    run(host="0.0.0.0", port=8080)

