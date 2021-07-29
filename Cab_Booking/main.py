import pickle
from Driver import Driver
from Rider import Rider
from distance import Distance

class Cab_booking:
    def __init__(self):

        print("\n$$$$$$$_____Code Written By Ankur Pandey_____$$$$$$$\n")

        self.user = input("Please enter R if you are a rider\nPlease enter D if you are a driver\nPlease enter Q if you want to exit from application\n").upper()
    def print_cab_booking(self):
        return self.user
    
    def User_Choice(self):

        if self.user == "R":
            Rider()
        
        elif self.user == "D":
            Driver()

        elif self.user == "Q":
            quit()
        
        else:
            print("Wrong input Please enter again")
            Cab_booking()
        


cab_obj=Cab_booking()
print(cab_obj.User_Choice())

# driver_obj=Driver()
# print(driver_obj.driver_details())

# rider_obj=Rider()

# print(rider_obj.rider_details())

# dist_obj=Distance()
# print(dist_obj.distance_input())
# print(dist_obj.total_distance())
# print(dist_obj.max_area())