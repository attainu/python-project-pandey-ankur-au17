class Driver:
    def __init__(self):
        self.name=input("Enter Driver Name:")
        self.age=int(input("Enter the Age:"))
        self.mobile_no=int(input("Enter the Mobile Number:"))
        self.driver_coord=int(input("Enter your Coordinates in x y with space")).split()
        self.driver_status=input("Available for booking yes or no :").upper()
        self.driver_tripStatus=False
        self.cab_driver=1
    def driver_details(self):
        return self.name,self.age,self.mobile_no,self.driver_coord,self.driver_status,self.driver_tripStatus,self.cab_driver
    
    def max_dist(self):
        self.max_distance = 100
        return self.max_distance


