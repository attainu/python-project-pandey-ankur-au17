class Avaiability():
    def Driver_Status_Updation(self):
        from Driver import Driver

        if self.driver_tripStatus == True:
            print("----------------------------------------------------\nYou have a ongoing trip.you can only change your status once your trip is ended.Please try after customer ends the trip.\n----------------------------------------------------")
            self.Driver_Account_Login_Page()
        else:
            y = input("Please enter AVAILABLE OR UNAVAILABLE : ").upper()

            if y == "UNAVAILABLE":
                self.driver_status = False
                print("your current status is : UNAVAILABLE, \n To recieve bookings please change your status.Thank you")
                print("----------------------------------------------------")
                self.Driver_Account_Login_Page()

            elif y == "AVAILABLE":
                self.driver_status = True
                print("your current status is : AVAILABLE, \n You will be randomly assigned to the nearest rider as soon as a new booking requirement comes.\n Thank You")
                print("----------------------------------------------------")
                self.Driver_Account_Login_Page()

            else:
                print("Wrong input.Please try again")
                self.Driver_Status_Updation()

obj=Avaiability()
print(obj.Driver_Status_Updation())