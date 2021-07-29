class Rider:
    def __init__(self):
        self.name=input("Enter Rider Name:")
        self.age=int(input("Enter the Age:"))
        self.mobile_no=int(input("Enter the Mobile Number:"))
        self.rider_coord=input("Enter your location in x y with space:").split()
        self.tripDetail=None
        self.trip_Id = None
        self.search_Status = None
        self.rider_Status = True

    def rider_details(self):
        return self.name,self.age,self.mobile_no,self.rider_coord,self.tripDetail,self.trip_Id,self.search_Status,self.rider_Status

