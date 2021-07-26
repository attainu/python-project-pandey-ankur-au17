import math
class Distance:
    def __init__(self):
        self.x1=None
        self.x2=None
        self.y1=None
        self.y2=None
    def distance_input(self):

        print("Your Location Cordinates")

        if self.x1==None:
            cord_1=int(input("Enter X1 cordinate:"))
            self.x1=cord_1

        if self.y1==None:
            cord_3=int(input("Enter Y1 cordinate:"))
            self.y1=cord_3

        print("your destination cordinates")

        if self.x2==None:
            cord_2=int(input("Enter X2 cordinate:"))
            self.x2=cord_2

        if self.y2==None:
            cord_4=int(input("Enter Y2 cordinate:"))
            self.y2=cord_4

        return self.x1,self.y1,self.x2,self.y2

    def total_distance(self):
        xy=math.sqrt(((self.x1-self.x2)**2)+((self.y1-self.y2)**2))
        return f"Total Distance is {format(xy, '.2f')} KM "
    
    def max_area(self):
        print("searching area of cab for a ride")
        rad = 6  #distance from Rider Location,maximum radius is 6 KM
        total_area=2*3.14*rad*rad
        return f"circumferance can search for cab from rider cordinates is : {format(total_area,'.2f')} KM"

