# level1:Level = Level(1, "truck", 5, ['A', 'B', 'C', 'D', 'E'])
# level1.entry()
# level1.park_vehicle("CA4661")
# level1.exit()

test = {'ca8923':'A' , 'fd5678': 'B', 'uh7658': 'C'}
print(test)
test2 = list(test.items())
print(test2)
a,b = {'ca8923':'A', 'fd5678': 'B'}
print(a)
print(b)

'''

- {'ca8923':'A' , 'fd5678': 'B', 'uh7658': 'C'}
- [('ca8923','A' ), ('fd5678', 'B'), ('uh7658', 'C')]
- ('ca8923','A')   
- a,b = 'ca8923','A'
- a,b = ['ca8923','A']


''' 

a:list[int] = []
b:list[int] = []
def check_array(a:list[int],b:list[int]):
    if a == b:
        print('same array')
    else:
        print('different array')
check_array([],[1,2])
check_array([1,2],[1,2])
check_array([])



'''   
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
    '''