#!/usr/bin/env python3
""" Module provides a Van class, a subtype of Vehicle class. """
from vehicle import Vehicle

class Van(Vehicle):
    """ 
    Subtype of the Vehicle class.

    Contains additional attributes of make and model, num of passengers.
    Supports polymorphic behaviour of method get_description.
    """
    
    def __init__(self, make_model, mpg, num_passengers, vin):
        """ (Van, str, str, str, str) -> str, str, bool, str, str

        Initializes with make-model, mpg, num_passengers, vin.
        """
        super().__init__(mpg, vin)  # Init Vehicle class

        self.__make_model = make_model
        self.__num_passengers = num_passengers
        
    def get_description (self):
        """ (Van) -> str
        
        Returns description of car as a formatted string.
        """
        spacing = '   '
        description = '{0:<22}{1}passengers: {2:>2}{1}{3}'.format(
            self.__make_model, spacing, self.__num_passengers, \
            Vehicle.get_description(self) )
        
        return description