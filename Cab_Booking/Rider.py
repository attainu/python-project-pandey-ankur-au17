import main
class Rider:
    def __init__(self):
        self.name=input("Enter Rider Name:")
        self.age=int(input("Enter the Age:"))
        self.mobile_no=int(input("Enter the Mobile Number:"))
        self.rider_coord=list(map(float,input("Please enter x , y coordinates with spaces").split()))
        self.tripDetail=None
        self.trip_Id = None
        self.search_Status = None
        self.rider_Status = True

    def rider_details(self):
        return self.name,self.age,self.mobile_no,self.rider_coord,self.tripDetail,self.trip_Id,self.search_Status,self.rider_Status

    def Rider_Account_Login_Page(self):
        print(f"----------------------------------------------------\nhi {self.name}.Welcome to your account.Please find the account details below.\n----------------------------------------------------")
        print(f"Name : {self.name}\nContact No : {self.mobile_no}\nYour current Position : {self.rider_coord} ")
        while True:
            try:
                no = int(input("please select an option from below.Please given option number as input \n 1-newbooking \n 2-history of rides \n 3-end current ongoing trip if any \n 4- to exit from your account\n"))
                break
            except Exception:
                print("Wrong input Please try again.")

        if no == 1:
            #self.Booking()
            pass
        
        if no == 2:
            #self.History()
            pass
        
        if no == 3:
            #self.End_Trip()
            pass
        
        if no == 4:
            main.Cab_booking()
        else:
            print("Wrong input.Routing you back to your account page.")
            self.Rider_Account_Login_Page()