#!/usr/bin/env python3
""" Module provides a Reservations class. """

from reservation import Reservation

class Reservations(object):
    """ Aggregating class has methods for maintaining rental resevations """
    
    def __init__(self):
        """ (Reservations) -> dict

        Inits empty collection of reservations, with credit card numbers 
        serving as the key values.
        """
        self.__reservations = dict()
        
    def is_reserved(self, vin):
        """ (Reservations, str) -> bool

        Returns True if reservation for vin, else returns False
        """
        return vin in self.__reservations
    
    def get_vin_for_reserved(self, credit_card):
        """ (Reservations, str) -> str

        Returns vin of vehicles reserved with credit_card
        """
        return self.__reservations[credit_card].get_vin()

    def add_reservation(self, resv):
        """ (Reservations, bool) -> Reservations

        Adds new reservation
        """
        self.__reservations[resv.get_credit_card()] = resv
        
    def find_reservation(self, credit_card):
        """ (Reservations, str) -> bool

        Returns True if reservation for credit_card, else returns False
        """
        return credit_card in self.__reservations
    
    def cancel_reservation(self, credit_card):
        """ (Reservations, str) -> Reservations

        Deletes reservation matching credit card number
        """
        del (self.__reservations[credit_card])