#!/usr/bin/env python3
"""This module provide a VehicleCost class."""

class VehicleCost(object):
    """
    This class provides the methods for maintaining rental costs
    """
    def __init__(self, daily_rate, weekly_rate, weekend_rate, free_miles, per_mile_chrg, insur_rate):
        """Initialzes rental rates, num free miles /mileage chrg/insur rate."""

        self.__daily_rate = daily_rate
        self.__weekly_rate = weekly_rate
        self.__weekend_rate = weekend_rate
        self.__free_miles = free_miles
        self.__per_mile_chrg = per_mile_chrg
        self.__insur_rate = insur_rate
        
    def get_daily_rate(self):
        """Returns daily rental rate of vehicle."""
        return float(self.__daily_rate)
    
    def get_weekly_rate(self):
        """Returns weekly rental rate of vehicle."""
        return float(self.__weekly_rate)
    
    def get_weekend_rate(self):
        """Returns weekend rental rate of vehicle."""
        return float(self.__weekend_rate)
    
    def get_free_miles(self):
        """Returns number of free miles for vehicle rental."""
        return int(self.__free_miles)
    
    def get_per_mile_charge(self):
        """Returns per mile charge for vehicle rental."""
        return float(self.__per_mile_chrg)
    
    def get_insurance_rate(self):
        """Returns daily insurance rate for vehicle."""
        return float(self.__insur_rate)
    
    def get_costs(self):
        """Returns a list containing all costs for vehicle."""
        return [self.__daily_rate, self.__weekly_rate,
                self.__weekend_rate, self.__free_miles,
                self.__per_mile_chrg, self.__insur_rate]

