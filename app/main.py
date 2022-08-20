from flask import Flask, render_template
import MySQLdb
import config
from models.profile import Profile
from models.experience import Experience
from models.education import Education

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

    len = cur.execute("SELECT * FROM experiences ORDER BY id ASC")
    result = cur.fetchall()

    expriences = []

    for r in result:
        exp = Experience()
        exp.create_data(r[1], r[2], r[3], r[4], r[5], r[6])
        expriences.append(exp)

    len = cur.execute("SELECT * FROM educations ORDER BY id ASC")
    result = cur.fetchall()

    educations = []

    for r in result:
        edu = Education()
        edu.create_data(r[1], r[2], r[3], r[4], r[5], r[6])
        educations.append(edu)

    return render_template("index.html", data={"profile": profile, "experiences": expriences, "educations": educations})
    # return render_template("index.html")


if __name__ == "__main__":
    app.run("0.0.0.0", 5050, debug=True)
