import random

'''
class lot
class vehicle
class lift
'''

class Driver:
    
    def __init__(self, license:str, n:str):
        self.license:str = license
        self.name:str = n
        
    def park_vehicle(self, total_driver:list[str], parking_option:list[int]):
        
        while True:
            allocate_spot:int = random.randrange(len(parking_option))
            for i in range (len(total_driver)):
                if 0 == parking_option[allocate_spot]:
                    continue
                else:
                    parking_option[allocate_spot] = parking_option[allocate_spot] + 1 
                    break
        
class Lift:
    def __init__(self, l_t:str, l:int):
        self.lift_type = l_t #stairs, elevator, escalator
        self.levels = l
        
        
class Vehicle:

    def __init__(self, plate_no:str, v_h:str):
        self.plate_no = plate_no
        self.vehicle_type = v_h
     
    
class Lot:
    def __init__(self, l:str, level:int, t_s:int, number:str, vehicle_type:str, lift_type:str, spots:list[int]):
        self.location:str = l
        self.levels:int = level
        self.total_spots:int = t_s
        self.spot_occupied:int = 0
        self.total_driver:list[Driver] = None
        
        self.vehicle = Vehicle(plate_no = number, v_h = vehicle_type)
        self.lift = Lift(l_t = lift_type, l = level)
        
        self.spot_number:list[int] = spots
        self.entry_vehicle = self.entry()
    
    def entry(self):  
        if self.total_spots > self.spot_occcupied:
            self.spot_occcupied = self.spot_occcupied + 1
            print("Spot available")
            self.driver.park_vehicle(self.spot_number, self.total_driver)
            
        else:
            print("No spot availalabe.")

    def store_driver(self, name:str, license:str):
        driver:Driver = Driver(name,license)
        self.total_driver.append(driver)
        
    def exit(self):
        exit_vehicle , spot = random.choice(list(self.spots_assigned.items())) #get random key and value to exit
        if spot in self.spots:
            index = self.spots.index(spot)
            self.spot_taken.remove(index)
            print(f"Vehicle {exit_vehicle} has been removed.")
        self.spot_occcupied = self.spot_occcupied - 1
   