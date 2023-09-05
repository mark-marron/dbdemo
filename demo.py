# run with flask --app demo run --debug

from flask import Flask
from database import get_db, close_db

app = Flask(__name__)

@app.route("/")
def index():
    db = get_db()
    people = db.execute("""SELECT *
                  FROM people""").fetchall()
    close_db(None)
    for person in people:
        print("name: ", person["name"], " age: ", person["age"])

    return "success"