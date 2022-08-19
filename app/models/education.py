class Education:
    def __init__(self):
        self.university = ""
        self.grade = ""
        self.field = ""
        self.start_date = ""
        self.end_date = ""
        self.description = ""

    def create_data(self, university, grade, field, start_date, end_date, description):
        self.university = university
        self.grade = grade
        self.field = field
        self.start_date = start_date
        self.end_date = end_date
        self.description = description
