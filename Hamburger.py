# Author: Spencer Boris
# Description: Hamburger Solo Attempt ._.
import random

# Step 1:  Create an Order class -- This will define a variable called burger_count and will include
# a method which creates a number randomly between 1 and 20

class Order:
    #Create a method which will return a random number between 1 and 20 as how many burgers were ordered
    def randomBurgers(self):
        return random.randint(1, 20)
    #Define burger_count using that method
    def __init__(self):
        self.__burger_count = self.randomBurgers()
    #Getter for burger count
    def getBurgerCount(self):
        return self.__burger_count

# Step 2: Create a Person class -- This will define a variable called customer_name
# This will also use a list of 9 names to randomly pull from .. use choice()

class Person:
    def randomName(self):
        asCustomers = ["Jefe", "El Guapo", "Lucky Day", "Ned Nederlander", "Dusty Bottoms", "Harry Flugleman", "Carmen", "Invisible Swordsman", "Singing Bush"]
        return random.choice(asCustomers)
    def __init__(self):
        self.__customer_name = self.randomName()
    def getName(self):
        return self.__customer_name

# Step 3: Create a Customer class -- inherited from the person class so use super in constructor to
# call the parent function.  Create a variable called order in the constructor as well that assigns
# an order object

class Customer(Person):
    def __init__(self):
        super().__init__()
        self.__order = Order()
    def Order(self):
        return self.__order
    
# Step 4: Create a variable for a queue, like a list or something
queueCustomer = []

# Step 5: Create a variable for a dictionary with key values of type "string" and values of type int
myDict = {}

# Step 6: Put 100 customers into the queue
for iCount in range(0, 100):
    queueCustomer.append(Customer())

# Step 7: Sort everything into the dictionary where Key = customer_name and value = burger_count
for customer in queueCustomer:
    if customer.getName() in myDict:
        custOrder = customer.Order()
        myDict[customer.getName()] += custOrder.getBurgerCount()
    else:
        custOrder = customer.Order()
        myDict[customer.getName()] = custOrder.getBurgerCount()

# Order them by burger count
BigBurger = list(myDict.values())
BigBurger.sort(reverse=True)

values = list(myDict.values())
keys = list(myDict.keys())
print("Name:\t\t\tOrder Count:\n")
for iCount in BigBurger:
    position = values.index(iCount)
    if len(keys[position]) < 8:
        print(f"{keys[position]}\t\t\t\t {values[position]}")
    elif len(keys[position]) >= 8 and len(keys[position]) < 19:
        print(f"{keys[position]}\t\t\t {values[position]}")
    else:
        print(f"{keys[position]}\t\t {values[position]}")
