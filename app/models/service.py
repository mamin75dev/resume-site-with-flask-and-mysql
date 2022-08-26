import MySQLdb
import config


class Service:
    def __init__(self):
        self.icon = ""
        self.title = ""
        self.description = ""

    def set_icon(self, icon):
        self.icon = icon

    def set_title(self, title):
        self.title = title

    def set_description(self, description):
        self.description = description

    @staticmethod
    def get_services_from_db():
        db = MySQLdb.connect(host=config.DB_HOST, user=config.DB_USER,
                             passwd=config.DB_PASS, db=config.DB_NAME)
        cur = db.cursor()
        services = []
        len = cur.execute("SELECT * FROM services")
        if len < 1:
            return services
        result = cur.fetchall()
        for row in result:
            service = Service()
            service.set_icon(row[1])
            service.set_title(row[2])
            service.set_description(row[3])
            services.append(service)
        return services
