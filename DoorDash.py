# Description: File for the group project
# Authors: Ben, Brad, Devan, Jared, Miles, Spencer

# Create Order class: Devan
# Create Person class: Jared
# Create Customer (Person) class: Devan
# Create Queue: Brad
# Create Dictionary: Spencer
# Print and Sort: Ben
# Proofreading: Miles

# Goal: Be done by Monday, Mar 6

print("Hey guys :)")
print("Testing")
print("This is the new stuff.")

# HEAD
print("This is another test")
# =======
# Get random module
import random

# Class for Person
class Person():
    # Constructor
    def __init__(self,customer_name):
        self.customer_name = self.randomName()
    
    # Random name method
    def randomName(self):
        # Create customer list
        asCustomers = ["Jefe", "El Guapo", "Lucky Day", "Ned Nederlander", "Dusty Bottoms", "Harry Flugleman", "Carmen", "Invisible Swordsman", "Singing Bush"]
        # Choose and return random name
        return random.choice(asCustomers)
# >>>>>>> 4194a83de4e821f5deb025d3a18f1341763ee0c1
