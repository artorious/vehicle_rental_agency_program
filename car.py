#!/usr/bin/env python3
""" Module provides a Car class, a subtype of Vehicle class. """
from vehicle import Vehicle
class Car(Vehicle):
    """ 
    Subtype of the Vehicle class.

    Contains additional attributes of make and model, num of passengers and
    num of doors. Supports polymorphic behaviour of method get_description.
    """
    
    def __init__(self, make_model, mpg, num_passengers, num_doors, vin):
        """ Initialized with provided parameters """
        super().__init__(mpg, vin)
        
        self.__make_model = make_model
        self.__num_passengers = num_passengers
        self.__num_doors = num_doors
    
    def get_description (self):
        """Returns description of car as a formatted string."""
        spacing = '   '
        description = '{0:<18}{1}passengers: {2}{1}doors: {3:<2}{1}{4}'.format(
            self.__make_model, spacing, self.__num_passengers, \
            self.__num_doors, Vehicle.get_description(self) )
        
        return description