import MySQLdb
import config


class Experience:
    def __init__(self):
        self.title = ""
        self.company_name = ""
        self.company_site = ""
        self.start_date = ""
        self.end_date = ""
        self.description = ""

    def set_title(self, title):
        self.title = title

    def set_company_name(self, company_name):
        self.company_name = company_name

    def set_company_site(self, company_site):
        self.company_site = company_site

    def set_start_date(self, start_date):
        self.start_date = start_date

    def set_end_date(self, end_date):
        self.end_date = end_date

    def set_description(self, description):
        self.description = description

    @staticmethod
    def get_expriences_from_db():
        db = MySQLdb.connect(host=config.DB_HOST, user=config.DB_USER,
                             passwd=config.DB_PASS, db=config.DB_NAME)
        cur = db.cursor()
        expriences = []
        len = cur.execute("SELECT * FROM experiences ORDER BY id ASC")
        if len < 1:
            return expriences
        result = cur.fetchall()
        for row in result:
            exp = Experience()
            exp.set_title(row[1])
            exp.set_company_name(row[2])
            exp.set_company_site(row[3])
            exp.set_start_date(row[4])
            exp.set_description(row[5])
            exp.set_description(row[6])
            expriences.append(exp)
        return expriences
