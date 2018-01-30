class SystemInterface :
	'''Provides all the methods that any user interface would need for interacting with the system (API)'''
	def __init__(self) :
		pass
	def create (self) :
		# returns 
		pass
	def num_avail_vehicles (self, vehicle_type) :
		# returns 
		pass
	def get_vehicle (self, vin) :
		# returns 
		pass
	def get_vehicle_types (self) :
		# returns 
		pass
	def get_vehicle_costs (self, vehicle_type) :
		# returns 
		pass
	def get_avail_vehicles (self, vehicle_type) :
		# returns 
		pass
	def is_reserved (self, vin) :
		# returns 
		pass
	def find_reservation (self, credit_card) :
		# returns 
		pass
	def add_reservation (self, vin) :
		# returns 
		pass
	def cancel_reservation (self, credit_card) :
		# returns 
		pass
	def calc_rental_cost (self, vehicle_type, rental_period, want_insurance, miles_driving) :
		# returns 
		pass
class Van (Vehicle) :
	'''subclass maintains specific information for vehicle type. Stores the maximum number of passengers'''
	def __init__(self) :
		pass
	def create (self, make_model, mpg, num_passengers, vin) :
		# returns 
		pass
	def get_description (self) :
		# returns 
		pass
class Car (Vehicle) :
	'''Subclass maintains specific information for vehicle type. Stores maximum number of passengers and number of doors'''
	def __init__(self) :
		pass
	def create (self, make_model, mpg, num_passengers, num_doors, vin) :
		# returns 
		pass
	def get_description (self) :
		# returns 
		pass
class Reservations :
	'''aggregating class has methods for maintaining it's collection of objects.'''
	def __init__(self) :
		pass
	def create (self, vehicles) :
		# returns 
		pass
	def is_reserved (self, vin) :
		# returns 
		pass
	def get_vin_for_reserved (self, credit_card) :
		# returns 
		pass
	def add_reservation (self, resv) :
		# returns 
		pass
	def find_reservation (self, name, addr) :
		# returns 
		pass
	def cancel_reservation (self, credit_card) :
		# returns 
		pass
class VehicleCosts :
	'''aggregating class has methods for maintaining it's collection of objects,  returns the cost of a specific vehicle type as a single string for display'''
	def __init__(self) :
		pass
	def create (self, vehicle_types) :
		# returns 
		pass
	def get_vehicle_cost (self, vehicle_type) :
		# returns 
		pass
	def add_vehicle_cost (self, veh_type, veh_cost) :
		# returns 
		pass
	def cal_rental_cost (self, vehicle_type, rental_period, want_insurance, miles_driving) :
		# returns 
		pass
class Vehicles :
	'''aggregating class maintains a collection of the corresponding object type. Has aggregating class has methods for maintaining it's collection of objects.'''
	def __init__(self) :
		pass
	def create (self) :
		# returns 
		pass
	def get_vehicle (self, vin) :
		# returns 
		pass
	def add_vehicle (self, vehicle) :
		# returns 
		pass
	def num_avail_vehicles (self, vehicle_type) :
		# returns 
		pass
	def get_avail_vehicles (self, vehicle_type) :
		# returns 
		pass
	def unreserve_vehicle (self, vin) :
		# returns 
		pass
class VehicleCost :
	'''It's create(__init__) method is passed six arguments; the daily/weekly/weekend rates, the number of free miles, the per mile charge, and the daily insurance rate to initialize the object with'''
	def __init__(self) :
		pass
	def create (self, daily_rate, weekly_rate, weekend_rate, free_miles, per_mile_chrg, insur_rate) :
		# returns 
		pass
	def get_daily_rate (self) :
		# returns 
		pass
	def get_weekly_rate (self) :
		# returns 
		pass
	def get_weekend_rate (self) :
		# returns 
		pass
	def get_free_daily_miles (self) :
		# returns 
		pass
	def get_per_mile_charge (self) :
		# returns 
		pass
	def get_insurance_rate (self) :
		# returns 
		pass
	def get_costs (self) :
		# returns 
		pass
class RentalAgencyUI :
	'''Text-based user interface. Initialized with a reference to the system interface'''
	def __init__(self) :
		pass
	def create (self, system) :
		# returns 
		pass
	def start (self) :
		# returns 
		pass
class Truck (Vehicle) :
	'''subclass maintains specific information for vehicle type. Stores it's length and the number of rooms of stoage it can hold'''
	def __init__(self) :
		pass
	def create (self, mpg, length, num_rooms, vin) :
		# returns 
		pass
	def get_description (self) :
		# returns 
		pass
class Vehicle :
	'''superclass maintains vehicle's type, VIN, and resrevation status'''
	def __init__(self) :
		pass
	def create (self, mpg, vin) :
		# returns 
		pass
	def get_type (self) :
		# returns 
		pass
	def get_vin (self) :
		# returns 
		pass
	def get_description (self) :
		# returns 
		pass
	def is_reserved (self) :
		# returns 
		pass
	def set_reserved (self, resreved) :
		# returns 
		pass
class Reservation :
	def __init__(self) :
		pass
	def create (self, name, address, credit_card, vin) :
		# returns 
		pass
	def get_name (self) :
		# returns 
		pass
	def get_addr (self) :
		# returns 
		pass
	def get_credit_card (self) :
		# returns 
		pass
	def get_vin (self) :
		# returns 
		pass
