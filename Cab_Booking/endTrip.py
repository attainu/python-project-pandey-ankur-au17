class EndTrip:
    def End_Trip(self):
        from Driver import Driver
        from Rider import Rider

        if self.ridername == True:
            print("----------------------------------------------------\nThere is no ogoing trip to end.\n----------------------------------------------------")
            self.Rider_Account_Login_Page()
        else:
            self.ridername = True
            self.destination = True
            self.tripstatus = False

            print("----------------------------------------------------\nYour Trip is ended.Thank you for your ride\n----------------------------------------------------")
            self.Rider_Account_Login_Page()

obj=EndTrip()
print(obj.End_Trip())