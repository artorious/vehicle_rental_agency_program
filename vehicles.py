#!/usr/bin/env python3
"""
Vehicles class module. Raises InvalidFileFormatError and InvalidVinError. 
"""
from vehicle import Vehicle
from car import Car
from van import Van
from truck import Truck

class InvalidVinError(Exception):
    """ Exception indicating that a provided vin not found. """
    pass

class Vehicles:
    """
    Aggregating class maintains a collection of Vehicle object 
    """
    def __init__(self):
        """ Initializes empty list of vehicles """
        pass
    
    def get_vehicle(self, vin):
        """ Returns Vehicle for provided vin, Raises InvalidVinError. """
        raise
    
    def add_vehicle(self, vehicle):
        """ Adds new vehicle to list of vehicles. """
        pass
        
    def num_avail_vehicles(self, vehicle_type):
        """ Returns number of available vehicles of vehicle_type. """
        return
    
    def get_avail_vehicles(self, vehicle_type):
        """
        Returns a list of unreserved Vehicles objects of vehicle_type. 
        """
        return
    
    def unreserve_vehicle(self, vin):
        """
        Sets reservation status of vehicle with vin to unreserved
        """
        pass