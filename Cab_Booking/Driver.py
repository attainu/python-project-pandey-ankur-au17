class Driver:
    def __init__(self):
        self.name=input("Enter Driver Name:")
        self.age=int(input("Enter the Age:"))
        self.mobile_no=int(input("Enter the Mobile Number:"))
        self.cab_driver=1
    def driver_details(self):
        return self.name,self.age,self.mobile_no
    
    def max_dist(self):
        self.max_distance = 100
        return self.max_distance
    
