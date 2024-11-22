class Session:
    def __init__(self, location, type, year, id):
        self.location = location
        self.type = type
        self.year = year
        self.id = id
    
    def __eq__(self, other):
        if isinstance(other, self):
            return self.location == other.location and self.type == other.type and self.year == other.year and self.id == other.id
        return False
    
    def __str__(self):
        return f"{self.location} {self.type} {self.year}"