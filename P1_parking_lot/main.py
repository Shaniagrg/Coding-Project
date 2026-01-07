import random

'''
class lot
class vehicle
class lift
'''
class Lift:
    def __init__(self, l_t:str, l:int):
        self.lift_type = l_t #stairs, elevator, escalator
        self.levels = l
        
        
class Vehicle:
    def __init__(self, v_s:list[str]):
        self.spots:list[str] = v_s
        self.spot_taken:set[int] = set()
        self.spots_assigned:dict[str,str] = {} #key is vehicle and value is given_spot_to_vehicle
    
    def park_vehicle(self,vehicle:str):
            while True:
                allocate_spot:int = random.randrange(len(self.spots))
                if allocate_spot in self.spot_taken:
                    continue
                else:
                    self.spot_taken.add(allocate_spot)
                    given_spot_to_vehicle:str = self.spots[allocate_spot]
                    self.spots_assigned[vehicle] = given_spot_to_vehicle
                    print(f"Vehicle {vehicle} took spot in Level:{self.level_number} [{given_spot_to_vehicle}]") 
                    break
    
class Lot:
    def __init__(self,l:int, t_s:int, vehicle_spot:list[str], lift_type:str):
        self.level_number:int = l
        self.total_spots:int = t_s
        self.spot_occupied:int = 0
        
        self.vehicle = Vehicle(v_s = vehicle_spot)
        self.lift = Lift(l_t=lift_type,l=l)
    
    def entry(self):  
        if self.total_spots > self.spot_occcupied:
            self.spot_occcupied = self.spot_occcupied + 1
            print("Spot available")
        else:
            print(f"No spot availalabe in level {self.level_number}")
    
    def exit(self):
        exit_vehicle , spot = random.choice(list(self.spots_assigned.items())) #get random key and value to exit
        if spot in self.spots:
            index = self.spots.index(spot)
            self.spot_taken.remove(index)
            print(f"Vehicle {exit_vehicle} has been removed.")
        self.spot_occcupied = self.spot_occcupied - 1
   