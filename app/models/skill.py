import MySQLdb
import config


class Skill:
    def __init__(self):
        self.title = ""
        self.logo = ""
        self.point = ""

    def set_title(self, title):
        self.title = title

    def set_logo(self, logo):
        self.logo = logo

    def set_point(self, point):
        self.point = int(point)

    @staticmethod
    def get_skills_from_db():
        db = MySQLdb.connect(host=config.DB_HOST, user=config.DB_USER,
                             passwd=config.DB_PASS, db=config.DB_NAME)
        cur = db.cursor()
        skills = []
        len = cur.execute("SELECT * FROM skills ORDER BY point DESC")
        if len < 1:
            return skills
        result = cur.fetchall()
        for row in result:
            skill = Skill()
            skill.set_title(row[1])
            skill.set_logo(row[2])
            skill.set_point(row[3])
            skills.append(skill)
        return skills
