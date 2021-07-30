from Driver import Driver
from Rider import Rider
# from distance import Distance
# from bookedCab import CabBooked
# from bookingHistory import History
from driverAvailbility import Avaiability
# from cabLocation import Location
# from endTrip import EndTrip

class Cab_booking(Driver,Avaiability):
    def __init__(self, **kwargs):
        #Rider.__init__(self, **kwargs)
        Driver.__init__(self,**kwargs)
        print("\n$$$$$$$_____Code Written By Ankur Pandey_____$$$$$$$\n")

        self.user = input("Please enter R if you are a rider\nPlease enter D if you are a driver\nPlease enter Q if you want to exit from application\n").upper()
    def print_cab_booking(self):
        #return self.user
        print(Driver.driver_details())
        
    
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

    def isavailable(self):
        return self.Driver_Status_Updation(self)




cab_obj=Cab_booking(driver_name="Deepak",driver_age=23,mobile_no=7854788558,driver_coord=[1,2],driver_status=False)
print(cab_obj.print_cab_booking())
# driver_obj=Driver()
# print(driver_obj.driver_details())
# print(driver_obj.max_dist())
# print(driver_obj.Driver_Account_Login_Page())