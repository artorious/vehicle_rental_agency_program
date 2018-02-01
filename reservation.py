#!/usr/bin/env python3
""" Module contains a Reservation class for storing details of a rental """

class Reservation(object):
    """ Class provides the methods for maintaining reservations info """

    def __init__(self, name, address, credit_card, vin):
        """ (Reservation, str, str, str, str) -> str, str, str, str
        
        Init a Reservation object with name, address, credit_card and vin
        """
        pass
    
    def get_name(self):
        """(Reservation) -> str

        Returns first and last name for reservation
        """
        return
    
    def get_address(self):
        """(Reservation) -> str

        Returns address for reservation
        """
        return
    
    def get_credit_card(self):
        """(Reservation) -> str

        Returns credit card on reservation
        """
        return
    
    def get_vin(self):
        """(Reservation) -> str

        Returns vehicle identification number reservation
        """
        return