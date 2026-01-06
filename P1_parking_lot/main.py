'''
class lot
class vehicle
class lift
'''

class Lot:
    def __init__(self,l:int, t_s:int):
        self.level_number:int = l
        self.total_spots:int = t_s
        self.spot_occupied:int = 0
        
        '''
        self.vehicle = Vehicle()
        self.lift = Lift()
        '''

    
    def entry(self):  
        if self.total_spots > self.spot_occcupied:
            self.spot_occcupied = self.spot_occcupied + 1
            print("Spot available")
        else:
            print(f"No spot availalabe in level {self.level_number}")