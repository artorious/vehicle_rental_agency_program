#!/usr/bin/env python3
""" Module provides a VehicleCosts class """

from vehicle_cost import VehicleCost

# symbol constants
daily_rental = 1
weekly_rental = 2
weekend_rental = 3

class VehicleCosts(object):
    """ Aggregating class provides methods for maintaining rental costs """
    def __init__(self):
        """ Initializes vehicle costs to empty """
        pass
    
    def get_vehicle_cost(self, vehicle_type):
        """ Returns VehicleCost object for the specified vehicle type """
        return
    
    def add_vehicle_cost(self, veh_type, veh_cost):
        """ Adds a vehicle cost object to dictionary with keyword veh_type """
        pass
    
    def calc_rental_cost(
        self, vehicle_type, rental_period, want_insurance, miles_driving):
        """ Returns estimates of rental cost for provided parameter values

        Returns dictionary with key values: {'base_charges', 'insur_rate',
                                            'num_free_miles', 'per_mile_charge',
                                            'estimated_mileage_charges'}
        """
        return
    