class Meeting:
    def __init__(self, name, year, id):
        self.name = name
        self.year = year
        self.id = id
    
    def __str__(self):
        return f"{self.name}"