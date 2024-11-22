class Driver:
    def __init__(self, name, number):
        self.name = name
        self.number = number
    
    def __str__(self):
        return f"{self.name} {self.number}"