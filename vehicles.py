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
    Aggregating class maintains a collection of Vehicle objects 
    """
    def __init__(self):
        """ Initializes empty list of vehicles """
        self.__vehicles = []
    
    def get_vehicle(self, vin):
        """ Returns Vehicle for provided vin, Raises InvalidVinError. """
        for vehicle in self.__vehicles:
            if vehicle.get_vin() == vin:
                return vehicle
        raise InvalidVinError
    
    def add_vehicle(self, vehicle):
        """ Adds new vehicle to list of vehicles. """
        self.__vehicles.append(vehicle)
        
    def num_avail_vehicles(self, vehicle_type):
        """ Returns number of available vehicles of vehicle_type. """
        return len(self.get_avail_vehicles(vehicle_type))
    
    def get_avail_vehicles(self, vehicle_type):
        """
        Returns a list of unreserved Vehicles objects of vehicle_type. 
        """
        return [veh for veh in self.__vehicles \
                if veh.get_type() == vehicle_type and not veh.is_reserved()]
    
    def unreserve_vehicle(self, vin):
        """
        Sets reservation status of vehicle with vin to unreserved
        """
        k = 0
        found = False

        while not found:
            if self.__vehicles[k].get_vin() == vin:
                self.__vehicles[k].set_reserved(False)
                found = True