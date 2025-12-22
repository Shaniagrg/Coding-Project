import random

class Level:
    def __init__(self, l:int, v:str, s_a:int, s:list[str]):
        self.level_number = l
        self.vehicle_type = v
        self.spot_available = s_a  # Tracks the number of spots available in this level
        self.spot_occcupied = 0  
        self.spots = s
        self.spots_taken = {}
        
    def entry(self):  
        if self.spot_available > 0:
            self.spot_available = self.spot_available - 1
            self.spot_occcupied = self.spot_occcupied + 1
        else:
            print(f"No spot availalabe in level {self.level_number}")
            
    def exit(self):
        self.spot_available = self.spot_available + 1
        self.spot_occcupied = self.spot_occcupied - 1
