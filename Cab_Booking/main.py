import pickle
from Cab_driver import Driver
from Cab_rider import Rider
from distance import Distance

class Cab_booking():
    def __init__(self):
        pass
    def print_cab(self):
        pass
    
cab_obj=Cab_booking()
print(cab_obj.print_cab())

driver_obj=Driver()
print(driver_obj.driver_details())

rider_obj=Rider()
print(rider_obj.rider_details())

dist_obj=Distance()
print(dist_obj.distance_input())
print(dist_obj.total_distance())
print(dist_obj.max_area())