from driverAvailbility import Avaiability
from cabLocation import Location

class Driver:
    def __init__(self):
        self.name=input("Enter Driver Name:")
        self.age=int(input("Enter the Age:"))
        self.mobile_no=int(input("Enter the Mobile Number:"))
        self.driver_coord=list(map(float,input("Please enter x , y coordinates with spaces").split()))
        self.driver_status=input("Available for booking yes or no :").upper()
        self.driver_tripStatus=False
        self.cab_driver=1
    def driver_details(self):
        return self.name,self.age,self.mobile_no,self.driver_coord,self.driver_status,self.driver_tripStatus,self.cab_driver
    
    def max_dist(self):
        self.max_distance = 100
        return self.max_distance

    def Driver_Account_Login_Page(self):
        print(f"-----------------------------\nhi {self.name}.Welcome to your account.Please find the account details below.\n-----------------------------\nName : {self.name} \nContactNo : {self.mobile_no} \nCab location : {self.driver_coord}")
        if self.driver_status:

            print("Status : Available to accept a ride-----------------------------")
        else:
            print("Status : Unavailable to accept a ride\n-----------------------------")

        while True:
            try:
                x = int(input(f"Please select an option from below and given option number as input \n 1.To change your Status \n 2.To update your Cabs location \n 3.To exit from your account and go to Main interface\n"))
                break
            except Exception:
                print("Wrong input.Please try again.")

        if x == 1:
            self.Driver_Status_Updation()
        
        elif x == 2:
            self.Driver_Location_Updation()
        
        elif x == 3:

            self.Cab_booking()

        
        else:
            print("Wrong input please try again.Routing you back to your account page")
            self.Driver_Account_Login_Page()


driver_obj=Driver()
print(driver_obj.driver_details())
print(driver_obj.max_dist())
print(driver_obj.Driver_Account_Login_Page())