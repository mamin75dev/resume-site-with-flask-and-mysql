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

    def create_data(self, first_name, last_name, address, phone_number, email, github_link, stackoverflow_link,
                    linkedin_link, twitter_link, facebook_link, instagram_link, about_me):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.phone_number = phone_number
        self.email = email
        self.github_link = github_link
        self.stackoverflow_link = stackoverflow_link
        self.linkedin_link = linkedin_link
        self.twitter_link = twitter_link
        self.facebook_link = facebook_link
        self.instagram_link = instagram_link
        self.about_me = about_me
