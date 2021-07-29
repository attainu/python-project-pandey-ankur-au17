import math
class Distance:
    def __init__(self):
        self.x1=None
        self.x2=None
        self.y1=None
        self.y2=None

    def total_distance(self):
        xy=math.sqrt(((self.x1-self.x2)**2)+((self.y1-self.y2)**2))
        return f"Total Distance is {format(xy, '.2f')} KM "
    
    def max_area(self):
        print("searching area of cab for a ride")
        rad = 6  #distance from Rider Location,maximum radius is 6 KM
        total_area=2*3.14*rad*rad
        return f"circumferance can search for cab from rider cordinates is : {format(total_area,'.2f')} KM"

