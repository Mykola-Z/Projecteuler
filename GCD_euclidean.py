# -*- coding: utf-8 -*-
"""
Created on Sun Dec 8 18:51:02 2019

@author: mzly903
"""

class Restaurant():
    def __init__ (self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type
        
    def describe(self):
        print (self.name + ' welcomes you!')
        print ('We cook ' + self.type + ' food' )
    def open_restaurant(self):
        print (self.name + ' is open')
        
pizza = Restaurant('Bagira', 'Italian')

burger = Restaurant ('McDuck', 'American')

jalapeno = Restaurant ('Bueno', 'Mexican')
        
Restaurant.describe(pizza)
Restaurant.open_restaurant(jalapeno)
Restaurant.open_restaurant(burger)

class User():
    def __init__ (self, given_name, last_name):
        self.name = given_name
        self.surname = last_name
    def describe_user(self):
        print ('Mama mia! This is ' + self.name + ' ' + self.surname)
    def greet_user(self):
        print ('Ciao Dear ' + self.name)
    
Rigo = User('Rodrigo', 'Buanaroti')
Dick = User ('Richard', 'Brenton')

User.greet_user(Rigo)
User.describe_user(Dick)
Restaurant.describe(pizza)

