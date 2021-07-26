class Rider:
    def __init__(self):
        self.name=input("Enter Rider Name:")
        self.age=int(input("Enter the Age:"))
        self.mobile_no=int(input("Enter the Mobile Number:"))
    def rider_details(self):
        return self.name,self.age,self.mobile_no

