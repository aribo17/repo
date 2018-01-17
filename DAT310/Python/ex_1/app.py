"""
Exercise #1: Top movies

@author: Krisztian Balog
"""

from flask import Flask, render_template
import mysql.connector

conn = mysql.connector.connect(user='root', password='TechAdmin111',
                               host='127.0.0.1', database='dat310')

cur = conn.cursor()
sql = ("SELECT * FROM movies")
cur.execute(sql)
for(movies) in cur:
    print("{}".format(movies))
cur.close()

app = Flask(__name__)




@app.route("/")
def index():
    return render_template("movies.html", movies=MOVIES)


if __name__ == "__main__":
    app.run()


conn.close()
