class CabBooked:
    def Booking(self):
            while True:
                try:
                    self.rider_coord=[10,20]
                    if self.rider_coord == [] or self.rider_coord[0] == None or self.rider_coord[1] == None:
                        raise Exception
                    break
                except Exception:
                    print("Wrong input Please try again.")
            self.rider_coord = self.rider_coord
            self.search_Status = self.Availability_Search()

            if   self.rider_Status == False:
                    print("----------------------------------------------------\nYou cannot book another ride while your current ride is still ongoing.\n Please end the trip to finish current ride and book another\n----------------------------------------------------")
                    self.Rider_Account_Login_Page()
            elif self.search_Status == 0:
                print("----------------------------------------------------\nNo Cab Drivers are available at this time.Please try after sometime.We regret the inconvenice caused\n----------------------------------------------------")
                self.Rider_Account_Login_Page()
            elif self.search_Status == 1:
                print("----------------------------------------------------\nThere are no nearest Cabs available.Please try after Sometime\n----------------------------------------------------")
                self.Rider_Account_Login_Page()
            else:
                self.rider_Status = False
                self.driver_status = False
                self.Trip_ID = int(str(self.Cust_Contact_no)[6:10])
                for y in self.Trip_Details.keys():
                    if self.Trip_ID == y:
                        self.Trip_ID += 1

                self.Current_LiveBooking_data = {"Trip_ID" : self.Trip_ID,"Driver_Name" :self.name ,"Rider_name" : self.name}
                print("Your Booking is confirmed \n","your Trip_ID is : ",self.Trip_ID,"\n" , "Your Driver name is : ",self.name,"\n")
                self.Current_LiveBooking_data = self.search_Status
                self.Rider_Account_Login_Page()

obj=CabBooked()
print(obj.Booking())