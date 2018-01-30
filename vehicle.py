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
        self.__mpg = mpg
        self.__vin = vin
        self.__reserved = False

    def get_type(self):
        """ (Vehicle) -> str
        
        Returns the type of vehicle (car, van, Truck.)
        """
        return type(self).__name__
    
    def get_vin(self):
	    """(Vehicle) -> str

        Returns the vin of vehicle
        """ 
	    return self.__vin
    
    def get_description(self):
        """(Vehicle) -> str
        
        Returns general description of car not specific to type.
        """
        description = 'mpg:{0:>3}   vin:{1:>12}'.format(self.__mpg, self.__vin)
        return description
    
    def is_reserved(self):
	    """Returns True if vehicle is reserved, otherwise, returns False""" 
	    return self.__reserved
    
    def set_reserved(self, resreved):
	    """Sets reserved flag of vehicle to provided Bolean Value""" 
	    self.__reserved = resreved