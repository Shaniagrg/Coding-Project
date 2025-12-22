import random

class Level:
    def __init__(self, l:int, v:str, s_a:int, s:list[str]):
        self.level_number = l
        self.vehicle_type = v
        self.spot_available = s_a  # Tracks the number of spots available in this level
        self.spot_occcupied = 0  
        
        self.spots = s
        self.spot_taken:set[int] = set()
        self.spots_assigned = {} #key is vehicle and value is given_spot_to_vehicle
        
    def entry(self):  
        if self.spot_available > 0:
            self.spot_available = self.spot_available - 1
            self.spot_occcupied = self.spot_occcupied + 1
        else:
            print(f"No spot availalabe in level {self.level_number}")

    def park_vehicle(self,vehicle):
            allocate_spot = random.randrange(len(self.spots))
            while True:
                if len(self.spot_taken) == len(self.spots):
                    print(f"All spots are occupied in Level {self.level_number}.")
                    break
                elif allocate_spot in self.spot_taken:
                    continue
                else:
                    self.spot_taken.add(allocate_spot)
                    given_spot_to_vehicle = self.spots[allocate_spot]
                    self.spots_assigned[vehicle] = given_spot_to_vehicle 
                    break
              
    def exit(self):
        self.spot_available = self.spot_available + 1
        self.spot_occcupied = self.spot_occcupied - 1