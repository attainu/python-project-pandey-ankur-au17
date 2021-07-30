class History:
    def History(self):
        if self.tripDetail == {}:
            print("----------------------------------------------------\nSorry there is no ride History to print.\n----------------------------------------------------")
            self.Rider_Account_Login_Page()
        else :
            print("Please find your Ride history below : ")
            for keys , values in self.tripDetail.items():
                print("----------------------------------------------------\nDriver_Name : ",self.tripDetail[keys]["Driver_Name"],"--","--","Driver_Contact_no : ",self.tripDetail[keys]["Driver_Contact_no"],"--","\n----------------------------------------------------")
            self.Rider_Account_Login_Page()
obj=History()
print(obj.History())