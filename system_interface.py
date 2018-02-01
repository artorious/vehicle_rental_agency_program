#!/usr/bin/env python3
""" Module provides SystemInterface class for the vehicle Rental Program
Provides all the methods that any user interface would need for interacting 
with the system (API)

    Vehicles File Format
    --------------------
    The format for the vehicles file contains comma-separated values with the
    indicated header lines for cars, vans, and trucks. 

        #CARS#
        make-model, mpg, num passengers, vin
        .
        #VANS#
        make-model, mpg, num passengers, vin
        .
        #TRUCKS#
        mpg, length, num rooms, vin
        .
    
    Vehicle Cost File Format
    ------------------------
    The format for the rental costs file includes a header line, followed
    by three lines of comma-separated values for cars, vans and trucks.
        
        daily, weekly, weekend, free miles, mileage charge, insurance
    
    The following exceptions are raised: IOError
"""

from vehicles import Vehicles, Car, Van, Truck
from vehicle_costs import VehicleCost, VehicleCosts
from reservations import Reservations

# Symbolic Constants
vehicle_types = ['Car', 'Van', 'Truck']
vehicles_filename = 'vehicles_stock.txt'
vehicle_cost_filename = 'rental_cost.txt'

# Exception class
class InvalidFileFormatError(Exception):
    """ Exception Indicating Invalid file in file_name """
    
    def __init__(self, header, file_name):
        """
        """
        pass
    
    def __str__(self):
        return

class SystemInterface(object):
    """
    Class provides the system interface of the rental system
    """
    
    def __init__(self):
        """
        Populates vehicles and rental costs from file. Raises IOError
        """
        pass
        
    def num_avail_vehicles(self, vehicle_type):
        """
        Returns the number of available vehicles. Returns 0 if no no. of
        vehicles available.
        """
        return
    
    def get_vehicle(self, vin):
        """
        Returns Vhicle type for given vin
        """
        return
    
    def get_vehicle_types(self):
        """
        Returns all vehicle types as a tuple of strings
        """
        return
    
    def get_vehicle_costs(self, vehicle_type):
        """
        Returns vehicle costs for provided vehicle type as a list.

            list of form [daily rate, weekly rate, weekend rate,
                            num free miles, per mile charge, insur rate]
        """
        return
    
    def get_avail_vehicles(self, vehicle_type):
        """
        Returns a list of description of uneserved vehicles
        """
        return
    
    def is_reserved(self, vin):
        """
        Returns reservation Flag (True/False)
        """
        return
    
    def find_reservation(self, credit_card):
        """
        Returns reservation made with credit card number
        """
        return
    
    def add_reservation(self, vin):
        """
        Creates reservation and marks vehicles as reserved
        """
        pass
        
    def cancel_reservation(self, credit_card):
        """
        Cancels reservation made with provided credit card
        """
        pass
        
    def calc_rental_cost(
        self, vehicle_type, rental_period, want_insurance, miles_driving):
        """
        Returns estimate of rental cost for provided parameter values

            Returns dictonary with key values: 
                {'base_charges', 'insur_rate', 'num_free_miles', 
                'per_mile_charge', 'estimated_mileage_charges'}
        """
        return

    # ----- Private method
    def __populate_vehicles(self, vehicle_cost_file):
        """
        Gets vehicles from vehicle_file. Raises InvalidFileFormatError
        """
        pass

    def __populate_costs(self, cost_file):
        """
        Populates RentalCosts objects from provided file object
        """
        pass

