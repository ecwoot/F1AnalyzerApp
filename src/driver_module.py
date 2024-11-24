class Driver:
    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.pos = 0

    def set_pos(self, position):
        self.pos = position
    
    def __str__(self):
        return f"{self.name} {self.number}"