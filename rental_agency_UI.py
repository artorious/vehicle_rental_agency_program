#!/usr/bin/env python3
""" 
Module provides a console interface for the rental agency system 
Method start begins execution of the interface. Raises IOError exception
Initialized with a reference to the system interface
"""
from system_interface import vehicle_types
from vehicles import InvalidVinError
from vehicle_costs import daily_rental, weekly_rental, weekend_rental
from reservations import Reservation


class RentalAgencyUI(object):
    """ Provides a console interface for the rental agency system """
    
    def __init__(self, system):
        """ Stores the provided reference to the vehicle rental system """
        pass
    
    def start(self):
        """ Begins the command loop """
        pass

    # Private methods
    def __display_welcome_screen(self):
        """ PRIVATE: Displays welcome message and general instructions. """
        pass

    def __display_menu(self):
        """ PRIVATE: Dispalys a list of menu options on the screen """
        pass
    
    def __get_selection(self, num_selections, prompt='Enter: '):
        """ PRIVATE: Returns user-entered value in range 1-num_selections."""
        return

    def __display_div_line(self, title=''):
        """ PRIVATE: Dispalys lines of dashes, with optioanl title. """
        pass
    
    def __execute_cmd(self, selection):
        """ PRIVATE: Executes command for provided menu selection """
        pass
    
    def __cmd_display_vehicle_types(self):
        """ PRIVATE: Displays vehicle types (Cars, Vans, Trucks). """
        pass
    
    def __cmd_display_vehicle_costs(self):
        """ PRIVATE: Dispalys renatl costs for Cars, Vans, Trucks. """

        pass
    
    def __cmd_display_vehicles(self, vehicle_type, numbered=False):
        pass

    def __cmd_display_specific_rental_cost(self):
        """ PRIVATE: Prompts user for  selections and rental costs. """

        pass

    def __cmd_make_reservation(self):
        """ PRIVATE: Prompts user for vehicle vin and reserves vehicle """

        pass
    
    def __cmd_cancel_reservation(self):
        """ PRIVATE: Prompts user for credit card and cancels reservation. """
        pass
    
    def __dispaly_vehicle_types(self):
        """ PRIVATE: Dispalys the numbered selections of vehicle types """
        pass
    
    def __get_rental_period(self):
        """ PRIVATE: prompts user for desired rental period.

        Returns tuple of the form (x, n), where x is one of daily_rental, 
        weekly_rental, weekend_rental, and n is the number of those units,
        e.g. (daily_rental, 3) three days of daily rental.
        """

        return 
    