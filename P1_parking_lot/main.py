import random

'''
class lot
class vehicle
class lift
'''

class Driver_vehicle:
    
    def __init__(self, license:str, n:str, p_n:str):
        self.license:str = license
        self.name:str = n
        self.plate_no:str = p_n
        
        
    def park_vehicle(self, parking_option:list[int]):
        while True:
            allocate_spot:int = random.randrange(len(parking_option))
            if 0 == parking_option[allocate_spot]:
                continue
            else:
                parking_option[allocate_spot] = parking_option[allocate_spot] + 1 
                break
        
class Lift:
    def __init__(self, l_t:str, l:int):
        self.lift_type = l_t #stairs, elevator, escalator
        self.levels = l
        
           
class Lot:
    def __init__(self, l:str, vehicle:str, level:int, t_s:int, lift_type:str, spots:list[int]):
        self.location:str = l
        self.vehicle = vehicle
        self.levels:int = level
        self.total_spots:int = t_s
        self.spot_occupied:int = 0
        self.total_driver:list[Driver_vehicle] = None
        
        self.lift = Lift(l_t = lift_type, l = level)
        
        self.spot_number:list[int] = spots
        self.entry_vehicle = self.entry()
    
    def entry(self):  
        if self.total_spots > self.spot_occcupied:
            self.spot_occcupied = self.spot_occcupied + 1
            print("Spot available")
            
        else:
            print("No spot availalabe.")

    def store_driver(self, name:str, license:str, plate_no:str):
        driver:Driver_vehicle = Driver_vehicle(license=license, n=name, p_n=plate_no)
        self.total_driver.append(driver)
        driver.park_vehicle(self.spot_number)
        
    
        
'''
lot --> entry --> store_driver --> store_vehicle
'''        
    
   