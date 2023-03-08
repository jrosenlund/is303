# Author: Spencer Boris
# Description: Hamburger Solo Attempt ._.
import random

# Step 1:  Create an Order class -- This will define a variable called burger_count and will include
# a method which creates a number randomly between 1 and 20

class Order:
    # Create a method which will return a random number between 1 and 20 as how many burgers were ordered
    def randomBurgers(self):
        return random.randint(1, 20)
    # Define burger_count using that method
    def __init__(self):
        self.__burger_count = self.randomBurgers()
    # Getter for burger count
    def getBurgerCount(self):
        return self.__burger_count

# Step 2: Create a Person class -- This will define a variable called customer_name
# This will also use a list of 9 names to randomly pull from .. use choice()

class Person:
    # Create a method which will choose a random name from a list of 9 and return that name
    def randomName(self):
        asCustomers = ["Jefe", "El Guapo", "Lucky Day", "Ned Nederlander", "Dusty Bottoms", "Harry Flugleman", "Carmen", "Invisible Swordsman", "Singing Bush"]
        return random.choice(asCustomers)
    # Define customer_name using that method
    def __init__(self):
        self.__customer_name = self.randomName()
    # Getter for customer name
    def getName(self):
        return self.__customer_name

# Step 3: Create a Customer class -- inherited from the person class so use super in constructor to
# call the parent function.  Create a variable called order in the constructor as well that assigns
# an order object

class Customer(Person):
    # Declare variable for order using previous class
    def __init__(self):
        super().__init__()
        self.__order = Order()
    # Create method to return order
    def Order(self):
        return self.__order
    
# Step 4: Create a variable for a queue, like a list or something
# Empty for now, will be updated with a queue later
queueCustomer = []

# Step 5: Create a variable for a dictionary with key values of type "string" and values of type int
# Also empty for now but will be updated later
myDict = {}

# Step 6: Put 100 customers into the queue -- Do this with a for loop in a range 0 - 100 that appends each run through
for iCount in range(0, 100):
    queueCustomer.append(Customer())

# Step 7: Sort everything into the dictionary where Key = customer_name and value = burger_count
# Use a for loop to run through each customer in the queue
for customer in queueCustomer:
    # Account for repeated names in the queue
    if customer.getName() in myDict:
        # Create a variable to capture the number of burgers ordered (repeat for new customers too in the else statement)
        custOrder = customer.Order()
        # Add to the dictionary using a key of the customer name and make the value += the burger order
        myDict[customer.getName()] += custOrder.getBurgerCount()
    else:
        custOrder = customer.Order()
        # For the new customers set an initial order count
        myDict[customer.getName()] = custOrder.getBurgerCount()

# Step 8: Order them by burger count
# Start by makinga list of the values (burger count)
BigBurger = list(myDict.values())
# Sort it in descending order
BigBurger.sort(reverse=True)

# Create lists of the original orders of the values and keys to get their index
values = list(myDict.values())
keys = list(myDict.keys())

# Formating to make the print look pretty
print("Name:\t\t\tOrder Count:\n")

# Create a for loop that finds the original position of the newly sorted list
for iCount in BigBurger:
    # Get the position
    position = values.index(iCount)
    # Use conditionals based on length of name to know how many tabs to put between the name and the order count
    # print a statement using the names and their order count with even spacing
    if len(keys[position]) < 8:
        print(f"{keys[position]}\t\t\t\t {values[position]}")
    elif len(keys[position]) >= 8 and len(keys[position]) < 19:
        print(f"{keys[position]}\t\t\t {values[position]}")
    else:
        print(f"{keys[position]}\t\t {values[position]}")
