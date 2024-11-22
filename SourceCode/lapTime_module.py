class Lap:
    def __init__(self, time, lap):
        self.time = time
        self.lap = lap
        #self.tyre = tyre

    def __str__(self):
        if self.time is None:
            return f"{self.lap}: No time for Lap 1"

        if self.time > 60.0:
            minutes = int(self.time // 60)
            seconds = float(self.time % 60)
            time = f"{minutes}:{seconds:06.3f}"
        else:
            time = f"{self.time:.2f}"
        
        return f"{self.lap}: {time}"


