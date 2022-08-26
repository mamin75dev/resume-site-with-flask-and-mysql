import MySQLdb
import config


class Profile:
    def __init__(self):
        self.first_name = ""
        self.last_name = ""
        self.address = ""
        self.phone_number = ""
        self.email = ""
        self.github_link = ""
        self.stackoverflow_link = ""
        self.linkedin_link = ""
        self.twitter_link = ""
        self.facebook_link = ""
        self.instagram_link = ""
        self.about_me = ""

    def set_first_name(self, first_name):
        self.first_name = first_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def set_address(self, address):
        self.address = address

    def set_phone_number(self, phone_number):
        self.phone_number = phone_number

    def set_email(self, email):
        self.email = email

    def set_github_link(self, github_link):
        self.github_link = github_link

    def set_stackoverflow_link(self, stackoverflow_link):
        self.stackoverflow_link = stackoverflow_link

    def set_linkedin_link(self, linkedin_link):
        self.linkedin_link = linkedin_link

    def set_twitter_link(self, twitter_link):
        self.twitter_link = twitter_link

    def set_facebook_link(self, facebook_link):
        self.facebook_link = facebook_link

    def set_instagram_link(self, instagram_link):
        self.instagram_link = instagram_link

    def set_about_me(self, about_me):
        self.about_me = about_me

    def get_proflie_from_db(self):
        db = MySQLdb.connect(host=config.DB_HOST, user=config.DB_USER,
                             passwd=config.DB_PASS, db=config.DB_NAME)
        cur = db.cursor()
        len = cur.execute("SELECT * FROM personal ORDER BY id DESC LIMIT 1")
        if len < 1:
            return "not_found"
        result = cur.fetchone()
        self.set_first_name(result[1])
        self.set_last_name(result[2])
        self.set_address(result[3])
        self.set_phone_number(result[4])
        self.set_email(result[5])
        self.set_github_link(result[6])
        self.set_stackoverflow_link(result[7])
        self.set_linkedin_link(result[8])
        self.set_twitter_link(result[9])
        self.set_facebook_link(result[10])
        self.set_instagram_link(result[11])
        self.set_about_me(result[12])
