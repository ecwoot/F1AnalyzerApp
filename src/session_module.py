class Session:
    def __init__(self, location, type, year, id):
        self.location = location
        self.type = type
        self.year = year
        self.id = id
    
    def __str__(self):
        return f"{self.location} {self.type} {self.year}"