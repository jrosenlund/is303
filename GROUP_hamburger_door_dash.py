# Bradley Grover
# IS 303 Section 002
# GROUP Assignment: Hamburger Door Dash
# Code Description: track how many burgers each driver delivers

import random
from queue import Queue

class Order:
    def __init__(self):
        self.intBurgerCount = self.randomBurgers()

    def randomBurgers(self):
        return random.randint(1, 20)

class Person:
    def __init__(self):
        self.customerName = self.randomName()

    def randomName(self):
        asCustomers = ["Jefe", "El Guapo", "Lucky Day", "Ned Nederlander", "Dusty Bottoms", "Harry Flugleman", "Carmen", "Invisible Swordsman", "Singing Bush"]
        return random.choice(asCustomers)

class Customer(Person):
    def __init__(self):
        super().__init__()
        self.order = Order()

# create a queue to hold the customers
queueCustomers = Queue()

# create a dictionary to hold the customer information
dictCustomers = {}

# add 100 customers to the queue
for i in range(100):
    # create a new customer object
    objCustomer = Customer()

    # add the customer to the queue
    queueCustomers.put(objCustomer)

    # update the customer information in the dictionary
    if objCustomer.customerName in dictCustomers:
        dictCustomers[objCustomer.customerName] += objCustomer.order.intBurgerCount 
    else:
        dictCustomers[objCustomer.customerName] = objCustomer.order.intBurgerCount 

# sort the customers by the number of burgers ordered
listSortedCustomers = sorted(dictCustomers.items(), key = lambda x: x[1], reverse = True)

# display the customer information
print("Customer Name".ljust(19), "Burgers Ordered") # make the result pretty
print("-" * 40)
for customer in listSortedCustomers:
    print(customer[0].ljust(19), str(customer[1]).rjust(14)) # make the results prettier