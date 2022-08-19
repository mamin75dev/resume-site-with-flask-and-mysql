from flask import Flask, render_template
import MySQLdb
import config
from models.profile import Profile

app = Flask(__name__)


@app.route("/")
def main():
    db = MySQLdb.connect(host=config.DB_HOST, user=config.DB_USER,
                         passwd=config.DB_PASS, db=config.DB_NAME)

    cur = db.cursor()
    len = cur.execute("SELECT * FROM personal ORDER BY id DESC LIMIT 1")
    if (len < 1):
        return ("404.html")  # TODO: add 404 file to templates
    result = cur.fetchone()
    print(result)
    profile = Profile()
    profile.create_data(
        result[1],
        result[2],
        result[3],
        result[4],
        result[5],
        result[6],
        result[7],
        result[8],
        result[9],
        result[10],
        result[11],
        result[12]
    )

    return render_template("index.html", data={"profile": profile})


if __name__ == "__main__":
    app.run("0.0.0.0", 5050, debug=True)
