import MySQLdb
import config


class Education:
    def __init__(self):
        self.university = ""
        self.grade = ""
        self.field = ""
        self.start_date = ""
        self.end_date = ""
        self.description = ""

    def set_university(self, university):
        self.university = university

    def set_grade(self, grade):
        self.grade = grade

    def set_field(self, field):
        self.field = field

    def set_start_date(self, start_date):
        self.start_date = start_date

    def set_end_date(self, end_date):
        self.end_date = end_date

    def set_description(self, description):
        self.description = description

    @staticmethod
    def get_educations_from_db():
        db = MySQLdb.connect(host=config.DB_HOST, user=config.DB_USER,
                             passwd=config.DB_PASS, db=config.DB_NAME)
        cur = db.cursor()
        educations = []
        len = cur.execute("SELECT * FROM educations ORDER BY id ASC")
        if len < 1:
            return educations

        result = cur.fetchall()
        for row in result:
            edu = Education()
            edu.set_university(row[1])
            edu.set_grade(row[2])
            edu.set_field(row[3])
            edu.set_start_date(row[4])
            edu.set_description(row[5])
            edu.set_description(row[6])
            educations.append(edu)

        return educations
