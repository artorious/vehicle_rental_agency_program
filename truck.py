#!/usr/bin/env python3
""" Module provides a Truck class, a subtype of Vehicle class. """
from vehicle import Vehicle

class Truck(Vehicle):
    """
    Subtype of Vehicle class

    Contains additional attributes length and num of rooms storage capacity.
    Supprs polyphormic behaviour of method get_description
    """
    def __init__(self, mpg, length, num_rooms, vin):
        """
        Initializes with mpg, length, num_rooms, vin.
        """
        super().__init__(mpg, vin)
        self.__length = length
        self.__num_rooms = num_rooms
        
    def get_description(self):
        """
        Returns complete description of truck
        """
        spacing = '   '
        description = 'length(feet):{0:>3}{1}{2:>2}{1}{3}'.format(self.__length, spacing, self.__num_rooms, Vehicle.get_description(self))

        return description