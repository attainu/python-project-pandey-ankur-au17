import pickle
from Driver import Driver
from Rider import Rider
from distance import Distance

class Cab_booking():
    def __init__(self):

        print("\n$$$$$$$_____Code Written By Ankur Pandey_____$$$$$$$\n")

        self.user = int(input("Please enter 1 if you are a rider\nPlease enter 2 if you are a driver\nPlease enter 3 if you want to exit from application\n"))
    def print_cab_booking(self):
        return self.user
    
    def User_Choice(self):

        if self.user == 1:
            Rider()
        
        elif self.user ==2:
            Driver() 

        elif self.user == 3:
            quit()
        
        else:
            print("Wrong input Please enter again")
            Cab_booking()
        


cab_obj=Cab_booking()
print(cab_obj)

# driver_obj=Driver()
# print(driver_obj.driver_details())

# rider_obj=Rider()

# print(rider_obj.rider_details())

# dist_obj=Distance()
# print(dist_obj.distance_input())
# print(dist_obj.total_distance())
# print(dist_obj.max_area())