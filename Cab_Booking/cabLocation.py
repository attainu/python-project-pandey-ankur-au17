from Driver import Driver
class Location:
    def Driver_Location_Updation(self):

    
        if  self.driver_tripStatus== True:
                print("----------------------------------------------------\nYou cannot update coordinates while your current trip is not ended.\n Please try after customer ends the trip\n----------------------------------------------------")
                self.Driver_Account_Login_Page()
            
        else:
            while True:
                try:
                    if self.driver_coord == [] or self.driver_coord[0] == None or self.driver_coord[1] == None:
                        raise Exception()
                    break
                except Exception:
                    print("Wrong input. Please try again")
            self.driver_coord = self.driver_coord
            print("coordinates updated sucessfully")
            self.Driver_Account_Login_Page()