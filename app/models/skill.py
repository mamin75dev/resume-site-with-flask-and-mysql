class Skill:
    def __init__(self):
        self.title = ""
        self.logo = ""
        self.point = ""

    def create_data(self, title, logo, point):
        self.title = title
        self.logo = logo
        self.point = int(point)
