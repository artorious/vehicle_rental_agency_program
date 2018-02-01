#!/usr/bin/env python3
""" Module provides a Reservations class. """

from reservation import Reservation

class Reservations(object):
    """ Aggregating class has methods for maintaining rental resevations """
    
    def __init__(self):
        """ (Reservations) - dict

        Inits empty collection of reservations
        """
        pass
        
    def is_reserved(self, vin):
        """ (Reservations, str) -> bool

        Returns True if reservation for vin, else returns False
        """
        return
    
    def get_vin_for_reserved(self, credit_card):
        """ (Reservations, str) -> str

        Returns vin of vehicles reserved with credit_card
        """
        return

    def add_reservation(self, resv):
        """ (Reservations, bool) -> Reservations

        Adds new reservation
        """
        pass
        
    def find_reservation(self, credit_card):
        """ (Reservations, str) -> bool

        Returns True if reservation for credit_card, else returns False
        """
        return
    
    def cancel_reservation(self, credit_card):
        """ (Reservations, str) -> Reservations

        Deletes reservation matching credit card number
        """
        pass