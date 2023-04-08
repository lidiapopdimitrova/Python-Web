class DVD:
    def __init__(self, name, id, creation_year, creation_month, age_restriction):
        self.name = name
        self.id = id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    def from_date(self, id: int, name: str, date: str, age_restriction: int):
        date_splited = date.split(".")
        return DVD(name, id, int(date_splited[1]), int(date_splited[2]))

    def __repr__(self):
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) has" \
               f" age restriction {self.age_restriction}. Status: {self.is_rented}"
        
        