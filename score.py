class Score:
    def __init__(self):
        self.points = 0
        self.wave_points = 0
    
    def add_points(self, n=1):
        self.points += n
        self.wave_points += n
    
    def reset_wave_points(self):
        self.wave_points = 0
    
    def get_total_points(self):
        return self.points
    
    def get_wave_points(self):
        return self.wave_points
