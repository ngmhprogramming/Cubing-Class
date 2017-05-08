#created by ngmh
#includes cube, cuber, record, and brand
#feel free to use this class and give credit
#include "from cubingClass import *" to reference
#includes test code in cuber example.py
#information as of 25/3/2017
#information may not be accurate
#too lazy to do research
print("cubingClass\n\
-------------------------\n\
created by ngmh\n\
includes cube, cuber, record, and brand\n\
feel free to use this class and give credit\n\
include 'from cubingClass import *' to reference\n\
includes test code in cuber example.py\n\
information as of 25/3/2017\n\
information may not be accurate\n\
too lazy to do research\n\
-------------------------\n")
class cuber(object):
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country
        self.brand = "None"
        self.records = []
        print("Cuber " + str(self.name) + " created")
    def get_name(self):
        return self.name
    def add(self, brand):
        self.brand = brand.name
        brand.add_cuber(self.name)
    def add_record(self, record):
        self.records.append(record)
    def __str__(self):
        return "Name: " + str(self.name) + "\nAge: " + str(self.age) + "\nCountry: " + str(self.country) + "\nBrand: " + str(self.brand)
class cube(object):
    def __init__(self, name,  size, cost):
        self.name = name
        self.size = size
        self.cost = cost
        self.brand = "None"
        print("Cube " + str(self.name) + " created")
    def add(self, brand):
        self.brand = brand.name
        brand.add(self.name)
    def getname(self):
        return self.name
    def __str__(self):
        return "Name: " + str(self.name) + "\nBrand: " + str(self.brand) + "\nSize: " + str(self.size) + "\nCost: " + str(self.cost)
class brand(object):
    def __init__(self, name, country):
        self.name = name
        self.country = country
        self.products = []
        self.cubers = []
        print("Brand " + str(self.name) + " created")
    def __str__(self):
        return "Name: " + str(self.name) + "\nCountry: " + str(self.country)
    def add(self, cube):
        self.products.append(cube)
        return "Added product " + str(cube) + " to brand " + str(self.name)
    def add_cuber(self, cuber):
        self.cubers.append(cuber)
        return "Added " + str(cuber) + " to brand " + str(self.name)
    def get_products(self):
        return self.products
    def get_cubers(self):
        return self.cubers
class record(object):
    def __init__(self, name, time, cuber):
        self.name = name
        self.time = time
        self.cuber = cuber.get_name()
        print("Record " + str(self.name) + " created")
        cuber.add_record([name, time])
    def __str__(self):
        return "Name: " + str(self.name) + "\nTime: " + str(self.time) + "\nCuber: " + str(self.cuber)
