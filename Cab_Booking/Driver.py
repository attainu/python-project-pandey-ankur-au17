class Driver:
    def __init__(self, **kwargs):
        self.name=kwargs.get('driver_name')
        self.age=kwargs.get('driver_age')
        self.mobile_no=kwargs.get('mobile_no')
        self.driver_coord=kwargs.get('driver_coord')
        self.driver_status=kwargs.get('driver_status')
        self.driver_tripStatus=False
        self.cab_driver=1
    def driver_details(self):
        return self.name,self.age,self.mobile_no,self.driver_coord,self.driver_status,self.driver_tripStatus,self.cab_driver
    
    def max_dist(self):
        self.max_distance = 100
        return self.max_distance

    def Driver_Account_Login_Page(self):
        from main import Cab_booking
        from cabLocation import Location
        from driverAvailbility import Avaiability

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

            Cab_booking()

        
        else:
            print("Wrong input please try again.Routing you back to your account page")
            self.Driver_Account_Login_Page()
# deepak=Driver(driver_name="Deepak",driver_age=23,mobile_no=7854788558,driver_coord=[1,2],driver_status=False)
# print(deepak.driver_details())