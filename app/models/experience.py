class Experience:
    def __init__(self):
        self.title = ""
        self.company_name = ""
        self.company_site = ""
        self.start_date = ""
        self.end_date = ""
        self.description = ""

    def create_data(self, title, company_name, company_site, start_date, end_date, description):
        self.title = title
        self.company_name = company_name
        self.company_site = company_site
        self.start_date = start_date
        self.end_date = end_date
        self.description = description
