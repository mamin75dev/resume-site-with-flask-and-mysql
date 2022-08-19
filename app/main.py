from flask import Flask, render_template
import MySQLdb

app = Flask(__name__)


@app.route("/")
def main():
    db = MySQLdb.connect()
    return render_template("index.html")


if __name__ == "__main__":
    app.run("0.0.0.0", 5050, debug=True)
