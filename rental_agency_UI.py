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
        """ (RentalAgencyUI, SystemInterface) -> SystemInterface 
        
        Stores the provided reference to the vehicle rental system
        """
        self.__system = system

    def start(self):
        """ (RentalAgencyUI) -> RentalAgencyUI, stdout
        
        This method begins the command loop when called. 
        That is, the repeated action of displaying the main menu, 
        getting the user’s selection, and executing the selected command. 
        The loop continues until a value of 7 (quits the program) is entered. 
        """
        self.__display_welcome_screen()
        self.__display_menu()

        selection = self.__get_selection(7)

        while selection != 7:
            self.__execute_cmd(selection)
            self.__display_menu()
            selection = self.__get_selection(7)

        print('Thank you for using the Friendly Rental Agency')

    # Private methods in support of the execution of commands in the start method.
    def __display_welcome_screen(self):
        """ (RentalAgencyUI) -> stdout

        PRIVATE: Displays welcome message and general instructions. 
        """
        print('*' * 78)
        print(format(' * Welcome to the Friendly Rental Agency * ', '^80'))
        print('*' * 78)

    def __display_menu(self):
        """ (RentalAgencyUI) -> stdout
        
        PRIVATE: Dispalys a list of menu options on the screen 
        """
        print('\n<<< MAIN MENU >>>')
        print('1 - Dispaly Vehicle Types')
        print('2 - Check rental costs')
        print('3 - Check available vehicles')
        print('4 - Get cost of specific rental')
        print('5 - Make a reservation')
        print('6 - Cancel a reservation')
        print('7 - Quit\n')
    
    def __get_selection(self, num_selections, prompt='Enter: '):
        """ (RentalAgencyUI, int, str) -> int

        PRIVATE: Returns user-entered value in range 1-num_selections.
        """
        valid_input = False

        selection = input(prompt)

        while not valid_input:
            try:
                selection = int(selection)

                if selection < 1 or selection > num_selections:
                    print('* Invalid Entry *\n')
                    selection = input(prompt)
                else:
                    valid_input = True
                
            except ValueError:
                selection = input(prompt)
        
        return selection

    def __display_div_line(self, title=''):
        """ (RentalAgencyUI, str) -> stdout

        PRIVATE: Dispalys lines of dashes, with optioanl title. """
        
        if len(title) != 0:
            title = ' {0} '.format(title)
        print('{0:-^78}'.format(title))
    
    def __execute_cmd(self, selection):
        """ (RentalAgencyUI, int) -> func ......................
        
        PRIVATE: Executes command for provided menu selection 
        """
        
        if selection == 1:  
            self.__cmd_display_vehicle_types()
        elif selection == 2:
            self.__cmd_display_vehicle_costs()
        elif selection == 3:
            self.___cmd_prompt_and_display_avail_vehicles()
        elif selection == 4:
            self.__cmd_display_specific_rental_cost()
        elif selection == 5:
            self.__cmd_make_reservation()
        elif selection == 6:
            self.__cmd_cancel_reservation()

    def __cmd_display_vehicle_types(self):
        """ (RentalAgencyUI) -> stdout
        
        PRIVATE: Displays vehicle types (Cars, Vans, Trucks). 
        """
        self.__display_div_line('Types of Vehicles Availble for Rent')
        self.__dispaly_vehicle_types()
        self.__display_div_line()
    
    def __cmd_display_vehicle_costs(self):
        """ (RentalAgencyUI) -> stdout

        PRIVATE: Dispalys rental costs for Cars, Vans, Trucks. 
        """
        empty_str = ''
        blank_char = ' '

        # Get vehicle type from user
        self.__dispaly_vehicle_types()
        vehicle_type_num = self.__get_selection(len(vehicle_types))
        vehicle_type = vehicle_types[vehicle_type_num - 1]

        # Set column headings
        row1_colheadings = '{0}{1:7}{2:10}{3:17} '.format(
            blank_char * 24, 'Free', 'Per Mile', 'Insurance')

        row2_colheadings = '{0:7}{1:8}{2:9}{3:7}{4:10}{5:17} '.format(
            'Daily', 'Weekly', 'Weekend', 'Miles', 'Charge', '(per day)')

        # get vehicle costs
        costs = self.__system.get_vehicle_costs(vehicle_type)

        # build costs line to display
        costs_str = empty_str

        field_widths = ('7', '8', '9', '7' '10', '17')
        
        for k in range(0, len(costs)):
            costs_str += format(costs[k], '<' + field_widths[k])
        
        # Display headings and costs line
        self.__display_div_line('Rental Charges for {0}s'.format(
            vehicle_type))
        print()
        print('{0}\n{1}\n{2}'.format(
            row1_colheadings, row2_colheadings, costs_str))
        self.__display_div_line()

    def __cmd_display_avail_vehicles(self, vehicle_type, numbered=False):
        """ (RentalAgencyUI, str, bool) -> stdout

        PRIVATE: Dispalys unreserved vehicles of selected type.
        When default argument is True, lists vehicles with sequential
        numbers at the start of the line of each vehicle description.
        """
        avail_vehicles_list = self.__system.get_avail_vehicles(vehicle_type)
        self.__display_div_line('Avalable {0}s'.format(vehicle_type))

        if avail_vehicles_list == []:
            print('* No vehicles availble of this type')
        
        elif numbered:
            k = 1
            for veh in avail_vehicles_list:
                print('{0}-{1}'.format(k, veh.get_description()))
                k += 1
        
        else:
            for veh in avail_vehicles_list:
                print(veh.get_description())
    
    def ___cmd_prompt_and_display_avail_vehicles(self):
        """ (RentalAgencyUI) -> stdout
        
        PRIVATE: Prompts user for vehicle type, and display all 
        available vehicles of that type.
        """
        self.__dispaly_vehicle_types()
        vehicle_type_num = self.__get_selection(len(vehicle_types))
        vehicle_type = vehicle_types[vehicle_type_num - 1]
        self.__cmd_display_avail_vehicles(vehicle_type)
        
    def __cmd_display_specific_rental_cost(self):
        """ (RentalAgencyUI) -> stdout
        
        PRIVATE: Prompts user for  selections and rental costs. 
        """
        # get vehicle type and rental period from user
        self.__dispaly_vehicle_types()
        vehicle_type_num = self.__get_selection(len(vehicle_types))
        vehicle_type = vehicle_types[vehicle_type_num -1]

        # Assign tuple e.g ('daily_rental', '4')
        rental_period = self.__get_rental_period()

        # prompt user for optional insurance
        want_insurance = input('Would you like the insurance? (y/n): ')

        while want_insurance not in ('y', 'Y', 'n', 'N'):
            want_insurance = input('Would you like the insurance? (y/n): ')
        
        # Convert to boolean value
        want_insurance = want_insurance in ('y', 'Y')

        # prompt user for num of miles expected to drive 
        print('\nNumber of miles expected to drive?')
        num_miles = self.__get_selection(1000, prompt='Miles: ')

        # calc base rental cost
        rental_cost = self.__system.calc_rental_cost(
            vehicle_type, rental_period, want_insurance, num_miles)
        
        # Display estimated rental cost
        print()
        self.__display_div_line('ESTIMATED {0} RENTAL COST'.format(
            vehicle_type))
        
        if want_insurance:
            print('Insurance rate of {0} per day'.format(
                rental_cost['insur_rate']))
        
        else:
            print('* You have opted out of insurance coverage *')

        if rental_period[0] == daily_rental:
            print('\nDaily rental for {0} days would be ${1:.2f}'.format(
                rental_period[1], rental_cost['base_charges'] ))

        elif rental_period[0] == weekly_rental:
            print('\nWeekly rental for {0} weeks would be ${1:.2f}'.format(
                rental_period[1], rental_cost['base_charges'] ))

        elif rental_period[0] == weekend_rental:
            print('\nWeekend rental is ${0:.2f}'.format(
                rental_cost['base_charges']))
        
        est_total_cost = rental_cost['base_charges'] + \
                        rental_cost['estimated_mileage_charges']
        
        print('''\n
        Your cost with an estimated mileage of {0} miles would be {1:.2f} 
        which includes {2} free miles and a charge of {3:.2f} per mile.
        '''.format(num_miles, est_total_cost, rental_cost['num_free_miles'], 
            rental_cost['per_mile_charge']))
        
        self.__display_div_line()

    def __cmd_make_reservation(self):
        """ (RentalAgencyUI) -> Reservation
        
        PRIVATE: Prompts user for vehicle vin and reserves vehicle 
        """
        # Get vehicle type
        self.__dispaly_vehicle_types()
        vehicle_type_num = self.__get_selection(len(vehicle_types))
        vehicle_type = vehicle_types[vehicle_type_num - 1]

        if self.__system.num_avail_vehicles(vehicle_type) == 0:
            print('Sorry - No available {0}s, at the moment'.format(
                vehicle_types[vehicle_type_num - 1]))

        else:
            self.__cmd_display_avail_vehicles(vehicle_type, numbered=True)
            avail_vehicles = self.__system.get_avail_vehicles(vehicle_type)

            valid_input = False

            while not valid_input:
                selected = input('\nEnter number of vehicle to reserve: ')

                if not selected.isdigit():
                    print('Please enter the number preceeding the vehicle')
                elif int(selected) < 1 or int(selected) > \
                        self.__system.get_avail_vehicles(vehicle_type):
                    print('\nINVALID SELECTION - Please re-enter: ')
                
                else:
                    valid_input = True
            
            vin = avail_vehicles[int(selected) - 1].get_vin()
            vehicle = self.__system.get_vehicle(vin)
            print(vehicle.get_description())

            vehicle.set_reserved(True)

            name = input('\nEnter first and last name: ')
            addr = input('Enter address: ')
            credit_card = input('nter credit card number: ')

            reserv = Reservation(name, addr, credit_card, vin)
            self.__system.add_reservation(reserv)
            print('* Reservation Made *')

    
    def __cmd_cancel_reservation(self):
        """ (RentalAgencyUI) -> Reservation

        PRIVATE: Prompts user for credit card and cancels reservation. 
        """
        credit_card = input('Please enter your credit card number: ')

        if self.__system.find_reservation(credit_card):
            print('Calling cancel_reservation of sys') # **********
            self.__system.cancel_reservation(credit_card)
            print('** RESERVATION CANCELLED ***')
        
        else:
            print('* Reservation not Found - Invalid Credit card Entered *')
    
    def __dispaly_vehicle_types(self):
        """ (RentalAgencyUI) -> stdout

        PRIVATE: Dispalys the numbered selections of vehicle types 
        """
        print('\nEnter type of vehicle')
        vehicle_types_tuple = self.__system.get_vehicle_types()

        k = 1

        for veh_type in vehicle_types_tuple:
            print('{0} - {1}'.format(k, veh_type))
            k += 1
        
        print()
    
    def __get_rental_period(self):
        """ (RentalAgencyUI) -> tuple
        
        PRIVATE: prompts user for desired rental period.

        Returns tuple of the form (x, n), where x is one of daily_rental, 
        weekly_rental, weekend_rental, and n is the number of those units,
        e.g. (daily_rental, 3) three days of daily rental.
        """
        print('\nEnter the rental period:')
        print('{0} - Daily, {1} - Weekly, {2} - Weekend\n'.format(
            daily_rental, weekly_rental, weekend_rental))
        
        valid_input = False

        while not valid_input:
            try:
                selection = int(input('Enter: '))

                while selection not in (
                        daily_rental, weekly_rental, weekend_rental):
                    print('* Incorrect entry. Please Re-enter *\n')
                    selection = int(input('Enter: '))

                if selection == daily_rental:
                    print('How many days do you need the vehicle?', end='')
                    num_days = self.__get_selection(14, prompt=' ')

                    if num_days > 6:
                        print('Why don\'t you consider a weekly renal?\n')
                    
                    return (daily_rental, num_days)

                elif selection == weekly_rental:
                    print('How many weeks do you need the vehicle? (1-3): ')
                    num_weeks = self.__get_selection(3, prompt='Weeks: ')

                    return (selection, num_weeks)
                
                elif selection == weekend_rental:
                    return (selection, 1)

            except ValueError:
                print('* Invalid Input - Number Expected *\n')

        
