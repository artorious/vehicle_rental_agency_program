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
        """ (VehicleCosts) -> dict

        Initializes vehicle costs to empty 
        """
        self.__vehicle_costs = dict()
    
    def get_vehicle_cost(self, vehicle_type):
        """ (VehicleCosts) -> VehicleCost

        Returns VehicleCost object for the specified vehicle type 
        """
        return self.__vehicle_costs[vehicle_type]
    
    def add_vehicle_cost(self, veh_type, veh_cost):
        """ (VehicleCosts, str, VehicleCost) -> VehicleCosts

        Adds a vehicle cost object to dictionary with keyword veh_type 
        """
        self.__vehicle_costs[veh_type] = veh_cost
    
    def calc_rental_cost(
        self, vehicle_type, rental_period, want_insurance, miles_driving):
        """ (VehicleCosts, str, tuple, bool, int) -> dict

        eturns estimates of rental cost for provided parameter values

        Returns dictionary with key values: {'base_charges', 'insur_rate',
                                            'num_free_miles', 'per_mile_charge',
                                            'estimated_mileage_charges'}
        """
        # get vehicle cost
        vehicle_cost = self.get_vehicle_cost(vehicle_type)

        # calc rental charges
        rental_time = rental_period[1]
        
        if rental_period[0] == daily_rental:
            rental_rate = vehicle_cost.get_daily_rate()
            rental_period_value = daily_rental
            rental_period_str = 'daily rental'
            rental_days = rental_time

        elif rental_period[0] == weekly_rental:
            rental_rate = vehicle_cost.get_weekly_rate()
            rental_period_value = weekly_rental
            rental_period_str = 'weekly rental'
            rental_days = rental_time * 7
        
        elif rental_period[0] == weekend_rental:
            rental_rate = vehicle_cost.get_weekend_rate()
            rental_period_value = weekend_rental
            rental_period_str = 'weekend rental'
            rental_days = 2

        # get free miles, per mile charge and insurance rate
        num_free_miles = vehicle_cost.get_free_miles()
        per_mile_charge = vehicle_cost.get_per_mile_charge()
        insurance_rate = vehicle_cost.get_insurance_rate()

        # Calc base rental charges
        base_rental_charges = rental_days * rental_rate +\
                                rental_days * insurance_rate
        
        miles_charged = miles_driving - num_free_miles

        if miles_charged < 0:
            miles_charged = 0
        
        estimated_mileage_charges = miles_charged * per_mile_charge

        return {'base_charges': base_rental_charges,
                'insur_rate': insurance_rate,
                'num_free_miles': num_free_miles,
                'per_mile_charge': per_mile_charge,
                'estimated_mileage_charges': estimated_mileage_charges}
    
    