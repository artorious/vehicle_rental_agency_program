#!/usr/bin/env python3
""" Module provides a vehicle class. """
class Vehicle(object):
    """Vehicle class holds the mpg, vin and reserved flag of a vehicle.
    
    Contains attributes common to all vehicles: mpg, vin, and reserved
    (Boolean). Provides polymorphic  behaviour for method get_description.
    """
    def __init__(self, mpg, vin):
        """(Vehicle, str, str) -> Vehicle
        
        Initializes a Vehicle object with <mpg> and <vin>
        """
        pass

    def get_type(self):
        """Returns the type of vehicle (car, van, Truck.)"""
        return
    
    def get_vin(self):
	    """Returns the vin of vehicle""" 
	    return
    
    def get_description(self):
	    """Returns general description of car not specific to type.""" 
	    return
    
    def is_reserved(self):
	    """Returns True if vehicle is reserved, otherwise, returns False""" 
	    return
    
    def set_reserved(self, resreved):
	    """Sets reserved flag of vehicle to provided Bolean Value""" 
	    pass