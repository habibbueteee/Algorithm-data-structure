# print("Habib")

# array = [10, 3, 7, 5,77]


# #random access: indexing

# # Finding the maximum number : Linear Search O(N)

# max = array[0]

# for num in array:
	# if num > max:
		# max = num
		
# print(max)

#------------------------------------------------------------------
# n =  int(input())
# if n%2:
	# print("Weird")
# elif (n%2)==0 and n in range(2,6):
	# print("Not Weird")
# elif (n%2)==0 and n in range(6,21):
	# print("Weird")

# elif (n%2)==0 and n >20:
	# print("Not Weird")

# def greet_user():
	# """Display a simple greeting"""
	# str = "Hello"
	# return str.upper()
	
	
# a=greet_user()
# print(a)

#---------------------------------------------------------------------
# class Dog():
	# """A simple attempt to model a dog"""
	
	# def __init__(self, name, age):
		# """Initializing name and age attributes"""
		# self.name = name
		# self.age = age

	# def sit(self):
		# """Simulate a dog sitting in response to a command"""
		# print(self.name.title()+ " is now sitting")
		
	# def roll_over(self):
		# """Simulate rolling over in response to a command"""
		# print(self.name.title()+" rolled over!") 


# my_dog = Dog('whilli', 6)

# print("My dog's name is "+ my_dog.name.title()+".")

# print("My dog's age is "+ str(my_dog.age)+".")

# my_dog.sit()
# my_dog.roll_over()


class Car():
	""""Represnting a Car"""
	def __init__(self, make, model, year):
		"""Initialize attributes to describe a car"""
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0
		
	def get_descriptive_name(self):
		"""Return a neatly formatted descriptive name."""
		long_name = str(self.year)+ " "+ self.make + " " + self.model
		return long_name.title()
	
	def read_odometer(self):
		"""Print a statement showing the car's mileage."""
		print("This car has "+ str(self.odometer_reading)+ " miles on it.")
	
class ElectricCar(Car):
	"""Represent aspects of a car, specific to electric vehicles."""
	
	def __init__(self, make, model, year):
		"""Initialize attriibutes of the parent class."""
		super().__init__(make, model, year)
		self.battery_size = 70
		
	def describe_battery(self):
		"""Print battery description"""
		print("This car has a "+ str(self.battery_size)+ " -kwh battery")
		
# my_new_car = Car('audi', 'a4',2016)
# print(my_new_car.get_descriptive_name())
# my_new_car.odometer_reading = 23
# my_new_car.read_odometer()		

my_tesla = ElectricCar('Tesla', 'T5', 2009)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()



































