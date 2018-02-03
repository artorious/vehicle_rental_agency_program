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
vehicle_types = ('Car', 'Van', 'Truck')
vehicles_filename = 'vehicles_stock.txt'
vehicle_costs_filename = 'rental_cost.txt'

# Exception class
class InvalidFileFormatError(Exception):
    """ Exception Indicating Invalid file in file_name 
    
    Allows typical I/O errors (such as file not found error) to be reported
    as errors specific to the file formatting requirements program.
    """
    
    def __init__(self, header, file_name):
        """ (InvalidFileFormatError, str, str) -> str"""
        self.__header = header
        self.__file_name = file_name
    
    def __str__(self):
        """ (InvalidFileFormatError) -> str

        Enables information to be displayed specific to the error (i.e which
        file header was expected and not found, in which file)        
        """
        return 'FILE FORMAT ERROR: File header {0} expected in file {1}'\
                    .format(self.__header, self.__file_name)

class SystemInterface(object):
    """
    Class provides the system interface of the rental system
    """
    
    def __init__(self):
        """ (SystemInterface) -> list, dict, dict, NoneType or file obj, 
                                file obj, Vehicles, VehicleCosts

        Populates vehicles and rental costs from file. Raises IOError

        Creates instances of the three aggregator classes of the system— 
            Vehicles, VehicleCosts, and Reservations. 
        Each is initially empty when created. 
        
        A try block attempts to open and read the files defined by 
        VEHICLES_FILENAME and VEHICLE_COSTS_FILENAME. If opened successfully,
        then each is read to populate the corresponding object. The exception 
        handler catches two types of exceptions,InvalidFileFormatError and 
        IOERROR.
        """
        # Init private vars
        self.__vehicles = Vehicles()
        self.__vehicle_costs = VehicleCosts()
        self.__reservations = Reservations()
        self.__vehicle_info_file = None

        try:
            self.__vehicle_info_file = open(vehicles_filename, 'r')
            self.__rental_cost_file = open(vehicle_costs_filename, 'r')
            
            self.__populate_vehicles(self.__vehicle_info_file)
            self.__populate_costs(self.__rental_cost_file)

        except InvalidFileFormatError as ifferr:
            print(ifferr)
            raise IOError

        except IOError:
            if self.__vehicle_info_file == None:
                print('FILE NOT FOUND: {0}'.format(vehicles_filename))
            
            else:
                print('FILE NOT FOUND: {0}'.format(vehicle_costs_filename))
            raise IOError
    
    # Getter methods
    def num_avail_vehicles(self, vehicle_type):
        """ (SystemInterface) -> list

        Returns the number of available vehicles. Returns 0 if no no. of
        vehicles available.
        """
        return self.__vehicles.get_avail_vehicles(vehicle_type)
    
    def get_vehicle(self, vin):
        """ (SystemInterface, str) -> Vehicle
        
        Returns Vehicle type for given vin
        """
        return self.__vehicles.get_vehicle(vin)
    
    def get_vehicle_types(self):
        """ (SystemInterface) -> tuple

        Returns all vehicle types as a tuple of strings
        """
        return vehicle_types
    
    def get_vehicle_costs(self, vehicle_type):
        """ (SystemInterface, str) -> list

        Returns vehicle costs for provided vehicle type as a list.

            list of form [daily rate, weekly rate, weekend rate,
                            num free miles, per mile charge, insur rate]
        """
        return self.__vehicle_costs.get_vehicle_cost(vehicle_type).get_costs()
    
    def get_avail_vehicles(self, vehicle_type):
        """ (SystemInterface, str) -> list

        Returns a list of descriptions of uneserved vehicles
        """
        avail_vehicles = self.__vehicles.get_avail_vehicles(vehicle_type)
        
        return [veh for veh in avail_vehicles]
    
    def is_reserved(self, vin):
        """ (SystemInterface, str) -> bool

        Returns reservation Flag (True/False)
        """
        return self.__reservations.is_reserved(vin)
    
    def find_reservation(self, credit_card):
        """ (SystemInterface, str) -> bool

        Returns reservation made with credit card number
        """
        return self.__reservations.find_reservation(credit_card)
    
    def add_reservation(self, resv):
        """ (SystemInterface, str) -> SystemInterface

        Creates reservation and marks vehicles as reserved
        """
        self.__reservations.add_reservation(resv)
        
    def cancel_reservation(self, credit_card):
        """ (SystemInterface, str) -> SystemInterface

        Cancels reservation made with provided credit card
        """
        vin = self.__reservations.get_vin_for_reserved(credit_card)

        self.__vehicles.unreserve_vehicle(vin)
        self.__reservations.cancel_reservation(credit_card)
        
    def calc_rental_cost(
        self, vehicle_type, rental_period, want_insurance, miles_driving):
        """ (SystemInterface, str, str, bool, str) -> dict

        Returns estimate of rental cost for provided parameter values
            Returns dictonary with key values: 
                {'base_charges', 'insur_rate', 'num_free_miles', 
                'per_mile_charge', 'estimated_mileage_charges'}
        """
        return self.__vehicle_costs.calc_rental_cost(
                vehicle_type, rental_period, want_insurance, miles_driving)

    # ----- Private methods
    def __populate_vehicles(self, vehicle_file):
        """ (SystemInterface, file) -> Vehicles

        Reads the info given by <vehicle_file>, the vehicles_filename and 
        populates the Vehicles instance. Raises InvalidFileFormatError.
        """
        empty_str = ''
        
        # Init vehicle string file headers
        vehicle_file_headers = ('#CARS#', '#VANS#', '#TRUCKS#')
        vehicle_type_index = 0

        # read first line of file (#CARS# expected)
        vehicle_str = vehicle_file.readline()
        vehicle_info = vehicle_str.rstrip().split(',')
        file_header_found = vehicle_info[0]
        expected_header = vehicle_file_headers[0]

        if file_header_found != expected_header:
            raise InvalidFileFormatError(expected_header, vehicles_filename)
        
        else:
            # Read next line of the file after #CARS# header line
            vehicle_str = vehicle_file.readline()

            while vehicle_str != empty_str:
                
                # Convert comma-separated string into list of strings
                vehicle_info = vehicle_str.rstrip().split(',')

                if vehicle_info[0][0] == '#':
                    vehicle_type_index += 1
                    file_header_found = vehicle_info[0]
                    expected_header = vehicle_file_headers[vehicle_type_index]

                    if file_header_found != expected_header:
                        raise InvalidFileFormatError(
                            expected_header, vehicles_filename)
                    
                else:
                    # Create new vehicle object of the proper type
                    if file_header_found == '#CARS#':
                        vehicle = Car(*vehicle_info)
                    
                    elif file_header_found == '#VANS#':
                        vehicle = Van(*vehicle_info)
                    
                    elif file_header_found == '#TRUCKS#':
                        vehicle = Truck(*vehicle_info)
                    
                    # Add new vehicle to Vehicles list
                    self.__vehicles.add_vehicle(vehicle)
                
                # Read next line of vehicle information
                vehicle_str = vehicle_file.readline()
    
    def __populate_costs(self, cost_file):
        """ (SystemInterface, file) -> VehicleCosts

        Reads info given by <cost_file> file object(vehicle_costs_filename), 
        and populates the VehicleCosts instance.
        
        """
        # Skip file header / read first line of file
        cost_file.readline()
        cost_str = cost_file.readline()

        for veh_type in vehicle_types:
            # Strip off newline (last) character and split into list
            cost_info = cost_str.rstrip().split(',')

            for cost_item in cost_info:
                cost_item = cost_item.strip()

                # Add Vehicle Type/Rental Cost key/ value to dictionary
                self.__vehicle_costs.add_vehicle_cost(
                    veh_type, VehicleCost(*cost_info))

                # read next line of vehicle costs
                cost_str = cost_file.readline()
                        

