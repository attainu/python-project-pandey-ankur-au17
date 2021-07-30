import time
import math

#Master Database of  Driver Details

def masterDatadriver(driver_name,Drivercontact_no,driver_coord,driver_status,Vehicle_no,Vehicle_Model_Name,driverTRipstatus):

    global Master_Driver
    Master_Driver[Drivercontact_no] = [driver_name,driver_coord,Drivercontact_no,driver_status,Vehicle_no,Vehicle_Model_Name,driverTRipstatus]

##################################################################################################################################################################################################################################################################################################################################################################


#Master Database of  Customer Details

def masterDataRider(Customer_Name,Customer_ContactNO,Status,cust_coord):
    global Master_Rider
    Master_Rider[Customer_ContactNO] =  [Customer_Name,Status,cust_coord,Customer_ContactNO]


##################################################################################################################################################################################################################################################################################################################################################################

#Driver class defination

class Driver():
    def __init__(self,driver_name,Drivercontact_no,
        driver_coordInList,
        Vehicle_no,Vehicle_Model_Name,driver_status):

        self.driver_name = driver_name
        self.Drivercontact_no = Drivercontact_no
        self.driver_coord = driver_coordInList
        self.Vehicle_Model_Name = Vehicle_Model_Name
        self.Vehicle_no = Vehicle_no
        self.driver_status = driver_status
        self.driverTRipstatus = False
        masterDatadriver(self.driver_name,self.Drivercontact_no,self.driver_coord,self.driver_status,self.Vehicle_no,self.Vehicle_Model_Name,self.driverTRipstatus)
    

##################################################################################################################################################################################################################################################################################################################################################################


    #Driver account login interface defination

    def driver_loginPage(self):
        print(f"################################\nhi {self.driver_name}.Welcome to your account.Please find the account details below.\n################################\nName : {self.driver_name} \nContactNo : {self.Drivercontact_no} \nVehicle No : {self.Vehicle_no}\nVehicle Model Name: {self.Vehicle_Model_Name}\nCab location : {self.driver_coord}")
        if self.driver_status:

            print("Status : Available to accept a ride\n################################")
        else:
            print("Status : Unavailable to accept a ride\n################################")

        while True:
            try:
                x = int(input(f"Please select an option from below and given option number as input \n 1.To change your Status \n 2.To update your Cabs location \n 3.To exit from your account and go to Main interface\n"))
                break
            except Exception:
                print("Wrong input.Please try again.")

        if x == 1:
            self.driver_statusUpdt()
        
        elif x == 2:
            self.driver_locationUpdt()
        
        elif x == 3:
            main_view()
        
        else:
            print("Wrong input please try again.Routing you back to your account page")
            self.driver_loginPage()


##################################################################################################################################################################################################################################################################################################################################################################
     
        
    #Method to change Driver availability.

    def driver_statusUpdt(self):
            global Master_Driver

            if Master_Driver[self.Drivercontact_no][6] == True:
                print("########################################################\nYou have a ongoing trip.you can only change your status once your trip is ended.Please try after customer ends the trip.\n########################################################")
                self.driver_loginPage()
            else:
                y = input("Please enter AVAILABLE OR UNAVAILABLE : ").upper()

                if y == "UNAVAILABLE":
                    Master_Driver[self.Drivercontact_no][3] = False
                    self.driver_status = False
                    print("your current status is : UNAVAILABLE, \n To recieve bookings please change your status.Thank you")
                    print("########################################################")
                    self.driver_loginPage()

                elif y == "AVAILABLE":
                    Master_Driver[self.Drivercontact_no][3] = True
                    self.driver_status = True
                    print("your current status is : AVAILABLE, \n You will be randomly assigned to the nearest rider as soon as a new booking requirement comes.\n Thank You")
                    print("########################################################")
                    self.driver_loginPage()

                else:
                    print("Wrong input.Please try again")
                    self.driver_statusUpdt()


##################################################################################################################################################################################################################################################################################################################################################################

    #Method to change Driver Location 

    def driver_locationUpdt(self):

        if Master_Driver[self.Drivercontact_no][6] == True:
                print("########################################################\nYou cannot update coordinates while your current trip is not ended.\n Please try after customer ends the trip\n########################################################")
                self.driver_loginPage()
            
        else:
            while True:
                try:
                    self.driver_coord = list(map(float,input("Please enter x , y coordinates with spaces").split()))

                    if self.driver_coord == [] or self.driver_coord[0] == None or self.driver_coord[1] == None:
                        raise Exception()
                    break
                except Exception:
                    print("Wrong input. Please try again")
            Master_Driver[self.Drivercontact_no][1] = self.driver_coord
            print("coordinates updated sucessfully")
            self.driver_loginPage()


##################################################################################################################################################################################################################################################################################################################################################################


#Rider class

class Rider(Driver):
    def __init__(self,Cust_name,Cust_Contact_no,cust_coord):
        self.Cust_name = Cust_name
        self.Cust_Contact_no = Cust_Contact_no
        self.cust_coord = cust_coord
        self.Trip_Details = {}
        self.Trip_ID = None
        self.Search_Status = None
        self.Cust_Status = True
        self.Cur_Driver_Key = None
        masterDataRider(self.Cust_name,self.Cust_Contact_no,self.Cust_Status,self.cust_coord)


##################################################################################################################################################################################################################################################################################################################################################################


    #Rider account login interface

    def rider_loginPage(self):
        print(f"########################################################\nhi {self.Cust_name}.Welcome to your account.Please find the account details below.\n########################################################")
        print(f"Name : {self.Cust_name}\nContact No : {self.Cust_Contact_no}\nYour current Position : {self.cust_coord} ")
        while True:
            try:
                no = int(input("please select an option from below.Please given option number as input \n 1-newbooking \n 2-history of rides \n 3-end current ongoing trip if any \n 4- to exit from your account\n"))
                break
            except Exception:
                print("Wrong input Please try again.")

        if no == 1:
            self.Booking()
        
        if no == 2:
            self.History()
        
        if no == 3:
            self.End_Trip()
        
        if no == 4:
            main_view()
        else:
            print("Wrong input.Routing you back to your account page.")
            self.rider_loginPage()



##################################################################################################################################################################################################################################################################################################################################################################

    # Method to search the nearest available Rriver 


    def availibility(self):

        global Master_Driver
        flag = 0
        for key , value in Master_Driver.items():
            if value[3] == True:
                Distance_Calculator = math.sqrt(((Master_Driver[key][1][0] - Master_Rider[self.Cust_Contact_no][2][0])**2) + ((Master_Driver[key][1][1] - Master_Rider[self.Cust_Contact_no][2][1])**2))
                if  Distance_Calculator > 8:
                    flag = 1
                    continue
                else:
                    value[3] = False
                    value[6] = True
                    return key
        return flag
    


##################################################################################################################################################################################################################################################################################################################################################################


    # Method to perfom booking operation for Rider


    def Booking(self):

            global Master_Driver
            while True:
                try:
                    self.cust_coord = list(map(float,(input("########################################################\nPlease enter your current cordinates x , y with spaces ").split())))
                    if self.cust_coord == [] or self.cust_coord[0] == None or self.cust_coord[1] == None:
                        raise Exception
                    break
                except Exception:
                    print("Wrong input Please try again.")
            Master_Rider[self.Cust_Contact_no][2] = self.cust_coord
            self.Search_Status = self.availibility()

            if  Master_Rider[self.Cust_Contact_no][1] == False:
                    print("########################################################\nYou cannot book another ride while your current ride is still ongoing.\n Please end the trip to finish current ride and book another\n########################################################")
                    self.rider_loginPage()
            elif self.Search_Status == 0:
                print("########################################################\nNo Cab Drivers are available at this time.Please try after sometime.We regret the inconvenice caused\n########################################################")
                self.rider_loginPage()
            elif self.Search_Status == 1:
                print("########################################################\nThere are no nearest Cabs available.Please try after Sometime\n########################################################")
                self.rider_loginPage()
            else:
                global x
                global currentBooking_data
                Master_Rider[self.Cust_Contact_no][1] = False
                Master_Driver[self.Search_Status][5] = True
                Master_Driver[self.Search_Status][3] = False
                self.Trip_ID = int(str(self.Cust_Contact_no)[6:10])
                for y in self.Trip_Details.keys():
                    if self.Trip_ID == y:
                        self.Trip_ID += 1

                currentBooking_data[self.Trip_ID] = {"Trip_ID" : self.Trip_ID,"driver_name" : Master_Driver[self.Search_Status][0],"Rider_name" : self.Cust_name,"Vehicle_No" : Master_Driver[self.Search_Status][4],"Date" : x }
                self.Trip_Details[self.Trip_ID] = {"Trip_ID" : self.Trip_ID,"driver_name" : Master_Driver[self.Search_Status][0] ,"Vehicle_No": Master_Driver[self.Search_Status][4],"Drivercontact_no": Master_Driver[self.Search_Status][2],"Date": x}
                print("Your Booking is confirmed \n","your Trip_ID is : ",self.Trip_ID,"\n" , "Your Driver name is : ",Master_Driver[self.Search_Status][0],"\n","Vehicle_No : ", Master_Driver[self.Search_Status][4] ,"\n","Drivercontact_no :" , Master_Driver[self.Search_Status][2] ,"\n","Date : " , x )
                self.Cur_Driver_Key = self.Search_Status
                self.rider_loginPage()



##################################################################################################################################################################################################################################################################################################################################################################


    #Method to end trip of the Rider

    def End_Trip(self):
            if Master_Rider[self.Cust_Contact_no][1] == True:
                print("########################################################\nThere is no ogoing trip to end.\n########################################################")
                self.rider_loginPage()
            else:
                Master_Rider[self.Cust_Contact_no][1] = True
                Master_Driver[self.Cur_Driver_Key][3] = True
                Master_Driver[self.Cur_Driver_Key][5] = False
                currentBooking_data.pop(self.Trip_ID)

                print("########################################################\nYour Trip is ended.Thank you for your ride\n########################################################")
                self.rider_loginPage()


##################################################################################################################################################################################################################################################################################################################################################################


    
    #Method to show the rider History


    def History(self):
        if self.Trip_Details == {}:
            print("########################################################\nSorry there is no ride History to print.\n########################################################")
            self.rider_loginPage()
        else :
            print("Please find your Ride history below : ")
            for keys , values in self.Trip_Details.items():
                print("########################################################\nTrip_ID : ",self.Trip_Details[keys]["Trip_ID"],"--","driver_name : ",self.Trip_Details[keys]["driver_name"],"--","Vehicle_No : ",self.Trip_Details[keys]["Vehicle_No"],"--","Drivercontact_no : ",self.Trip_Details[keys]["Drivercontact_no"],"--","Date : ",self.Trip_Details[keys]["Date"],"\n########################################################")
            self.rider_loginPage()


##################################################################################################################################################################################################################################################################################################################################################################


class Admin:

    def __init__(self,Admin_Name,Admin_ContactNo):
        self.Admin_Name = Admin_Name
        self.Admin_ContactNo = Admin_ContactNo
    
    #Method to show interface of Admin Account Login page
    def admin_loginPage(self):
        print(f"################################\nhi {self.Admin_Name}.Welcome to your account.Please find the account details below.\n################################\nName : {self.Admin_Name} \nContactNo : {self.Admin_ContactNo}")

        while True:
            try:
                x = int(input(f"Please select an option from below and given option number as input \n 1.To view all the Current Ongoing Trips\n 2.To view all the registered Riders and Drivers data\n 3.To exit from your account and go to Main interface\n"))
                break
            except Exception:
                print("Wrong input.Please try again.")

        if x == 1:
            self.All_Ongoing_Trips()
        
        elif x == 2:
            self.All_RidersAndDrivers_Info()
        
        elif x == 3:
            main_view()
        
        else:
            print("Wrong input please try again.Routing you back to your account page")
            self.admin_loginPage()


##################################################################################################################################################################################################################################################################################################################################################################


    
    #Method to show all ongoing trips

    def All_Ongoing_Trips(self):
        print("################################\nPlease find below the list of all ongoing Trips :\n################################")
        if currentBooking_data == {}:
            print("Currently there are no on-going rides")
        else: 
            for key , value in currentBooking_data.items():
                print(value)
        self.admin_loginPage()


##################################################################################################################################################################################################################################################################################################################################################################


    #Method to show all Riders and Drivers Info

    def All_RidersAndDrivers_Info(self):
        print("################################\nPlease find the list of all Registered Riders and Drivers :\n################################")
        print("Riders info : \n-----------------")
        if masterRider_U == {}:
            print("Currently no Riders are present in the database")
        else:    
            for key , value in masterRider_U.items():
                print("[Rider name : ",value.Cust_name,",","Rider Contact No : ",value.Cust_Contact_no,"]")
        print("Drivers info : \n-----------------")
        if masterDriver_U == {}:
            print("Currently no Drivers are present in the database")
        else:
            for key , value in masterDriver_U.items():
                print("[Driver name: ",value.driver_name,",","Driver Contact No : ",value.Drivercontact_no,", Driver Vehicle No : ",value.Vehicle_no,", Vehicle Model Name : ",value.Vehicle_Model_Name,"]")
        
        self.admin_loginPage()



##################################################################################################################################################################################################################################################################################################################################################################


#Function for Rider interface

def rider_view():
        print("################################\nWelcome to Rider Interface\n################################")
        New_Existing = input("Please enter [N] if you new user\nEnter [O] to go to your existing account\nenter [E] to go to main interface\n").upper()
        if New_Existing == "N":
            while True:
                try:
                    name = input("Please enter your name : ")
                    if name.strip() == "":
                        raise Exception()
                    else:
                        break
                except Exception:
                    print("Name cannot be blank.Please try again")
            while True:
                try:
                    ContactNo = int(input("Please enter your contact no : "))
                    if len(str(ContactNo)) < 10:
                        raise Exception()
                    break
                except Exception:
                    print("You have entered wrong input or mobile no is not 10 digits.Please try again")
            while True:
                try:
                    Cust_coordinates = list(map(float,(input("Please enter your current cordinates x , y with spaces : ").split())))
                    if Cust_coordinates == [] or Cust_coordinates[0] == None or Cust_coordinates[1] == None:
                        raise Exception()
                    break
                except Exception:
                    print("You have entered wrong input.Please try again")
            masterRider_U[ContactNo] = Rider(name,ContactNo,Cust_coordinates)
            masterRider_U[ContactNo].rider_loginPage()
        elif New_Existing == "O":
            while True:
                try:
                    contactno = int(input("Please enter your registered contact no : "))
                    if len(str(contactno)) < 10:
                        raise Exception()
                    break
                except Exception:
                    print("You have entered wrong input or Mobile no is not 10 digits.Please try again")
            if contactno not in masterRider_U.keys():
                print("################################\nYou are not a registered user.Please create a account to continue.\n You are now routed to Rider interface\n################################")
                rider_view()
            else:
                masterRider_U[contactno].rider_loginPage()

        elif New_Existing == "E":
            main_view()

        else:
            print("################################\nWrong input.You are routed back to rider_view.Enter again.")
            rider_view()


##################################################################################################################################################################################################################################################################################################################################################################


#function for Driver Interface

def driver_view():

        print("################################\nWelcome to Driver Interface.\n################################") 
        New_Existing = input("Please enter [N] if you new user\nEnter [O] to go to your existing account\nenter [E] to go to main interface\n").upper()

        if New_Existing == "N":
            while True:
                try:
                    name = input("Please enter your name : ")
                    if name.strip() == "":
                        raise Exception()
                    else:
                        break
                except Exception:
                    print("Name cannot be blank.Please try again")
            while True:
                try:
                    ContactNo = int(input("Please enter your contact no : "))
                    if len(str(ContactNo)) < 10:
                        raise Exception()
                    break
                except Exception:
                    print("You have entered wrong input or Mobile no is not 10 digits.Please try again")
            while True:
                try:
                    cur_cordinates = list(map(float,input("Please enter your cordinates x , y with spaces : ").split()))
                    if cur_cordinates == [] or cur_cordinates[0] == None or cur_cordinates[1] ==None:
                        raise Exception()
                    break
                except Exception:
                    print("You have entered wrong input.Please try again")
            while True:
                try:
                    vehicleNo = input("Please enter your vehicle no : ")
                    if vehicleNo.strip() == "":
                        raise Exception()
                    else:
                        break
                except Exception:
                    print("Name cannot be blank.Please try again")
            while True:
                try:
                    ModelName = input("Please enter your Model Name : ")
                    if ModelName.strip() == "":
                        raise Exception()
                    else:
                        break
                except Exception:
                    print("Name cannot be blank.Please try again")
            
            while True:
                try:
                    availability = input("Please enter your Availability.enter yes if available,no if not : ").upper()
                    if availability.strip() == "":
                        raise Exception()
                    elif availability != "YES" and availability != "NO":
                        raise Exception()
                    else:
                        break
                except Exception:
                    print("Wrong input.Please try again")
            if availability == "YES":
                availability = True
            else:
                availability = False
            masterDriver_U[ContactNo] = Driver(name,ContactNo,cur_cordinates,vehicleNo,ModelName,availability)
            masterDriver_U[ContactNo].driver_loginPage()


        elif New_Existing == "O":
            while True:
                try:
                    contactno = int(input("Please enter your registered contact no : "))
                    if len(str(contactno)) < 10:
                        raise Exception()
                    break
                except Exception:
                    print("You have entered wrong input or Mobile no is not 10 digits.Please try again")
            if contactno not in masterDriver_U.keys():
                print("################################\nYou are not a registered user.Please create a account to continue.\n You are now routed to Driver Interface.\n################################")
                driver_view()
            else:
                masterDriver_U[contactno].driver_loginPage()
        elif New_Existing == "E":
            main_view()

        else:
            print("################################\nWrong input.Enter again\n################################")
            driver_view()


##################################################################################################################################################################################################################################################################################################################################################################



#Function for Admin interface

def admin_view():
    print("################################\nWelcome to Administrator Interface.\n################################") 
    New_Existing = input("Please enter [N] if you new user\nEnter [O] to go to your existing account\nenter [E] to go to main interface\n").upper()
    if New_Existing == "N":
            while True:
                try:
                    name = input("Please enter your name : ")
                    if name.strip() == "":
                        raise Exception()
                    else:
                        break
                except Exception:
                    print("Name cannot be blank.Please try again")
            while True:
                try:
                    ContactNo = int(input("Please enter your contact no : "))
                    if len(str(ContactNo)) < 10:
                        raise Exception()
                    break
                except Exception:
                    print("You have entered wrong input or Mobile no is not 10 digits.Please try again")
            
            Master_Admin[ContactNo] = Admin(name ,ContactNo)
            Master_Admin[ContactNo].admin_loginPage()
    elif New_Existing == "O":
        while True:
            try:
                contactno = int(input("Please enter your registered contact no : "))
                if len(str(contactno)) < 10:
                    raise Exception()
                break
            except Exception:
                print("You have entered wrong input.Please try again")
        if contactno not in Master_Admin.keys():
            print("################################\nYou are not a registered user.Please create a account to continue.\n You are now routed to Rider interface\n################################")
            admin_view()
        else:
            Master_Admin[contactno].admin_loginPage()

    elif New_Existing == "E":
        main_view()

    else:
        print("################################\nWrong input.You are routed back to rider_view.Enter again.")
        admin_view()


##################################################################################################################################################################################################################################################################################################################################################################



#Function for main interface.


def main_view():
    global masterDriver_U
    global masterRider_U
    print("\n$$$$$$$$$$$$$$$$_____Cab Booking System_____$$$$$$$$$$$$$$$$\n_______________________________________________________________Made by:-ANKUR PANDEY\n")
    user = (input("Please enter R if you are a Rider\nPlease enter D if you are a Driver\nPlease enter A if you are an Administrator\nPlease enter E if you want to Exit from Application\n")).upper()
    if user == "R":
        rider_view()
    
    elif user =="D":
        driver_view()

    elif user == "A":
        admin_view()  

    elif user == "E":
        quit()
    
    else:
        print("Wrong input Please enter again")
        main_view()
    


##################################################################################################################################################################################################################################################################################################################################################################



if __name__ == "__main__":
   x = time.strftime("%d/%m/%y")  
   masterRider_U = {}
   masterDriver_U = {}
   Master_Rider = {}
   Master_Driver = {}
   Master_Admin = {}
   currentBooking_data = {}
   main_view()
