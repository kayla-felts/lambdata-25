'''Module 1 OOP Example module'''
import pandas as pd

class My_DataFrame(pd.DataFrame):
    def say_hello(self):
        return 'Hi! I am a dataframe!'

class BareMinimumClass:
    pass


class Complex:
    '''
    This is a complex class that has a real and imaginary attribute
    '''

    def __init__(self, realpart, imag_part):
        ''''
        constructor for complex numbers
        '''
        self.r = realpart #complex_Object.r
        self.i = imag_part #complex_Object.i

    def add(self, other_complex):
        '''
        adds two complex objects together
        '''
        self.r += other_complex.r
        self.i += other_complex.i 

def __repr__(self):
    return '{},{}'.format(self.r,self.i)

class SocialMediaUser:
    def __init__(self, name, location, upvotes=0, secondary_upvotes=0, total_upvotes):
        self.name = name
        self.location = location
        self.upvotes = upvotes
        self.secondary_upvotes = upvotes + secondary_upvotes
        self.total_upvotes = upvotes + secondary_upvotes

    def recieve_upvotes(self, num_upvotes):
        self.upvote += int(num_upvotes)
        

     def is_popular(self):
       return self.total_upvotes > 100

class Animal:
    ''''General representation of an animal'''
    def __init__(self, name, weight, diet_type):
        self.name = str(name)
        self.weight = float(weight)
        self.diet_type = str(diet_type)

    def run(self):
        return 'Vrrom, Vroom, I go quick!'
    
    def eat(self, food):
        return 'Huge fan of that: {food}'

    def __repr__(self):
        return 'I am an animal named {self.name}'

class Sloth(Animal):
    def __init__(self, name, weight, diet_type, num_naps):
        super().__init__(name, weight, diet_type)
        self.num_naps = int(num_naps)

    def say_somehting(self):
        return 'This is a sloth of typing!'

    def run(self):
        return 'I am a slow guy'
    

if __name__ == '__main__':  
    complex_num_2_object = Complex(3, -5) 
    # Complex_num_1_object.r = 3
    # Complex_num_1_object.i = -5

    complex_num_1_object = Complex(2, 6) 

    complex_num_1_object.add(complex_num_2_object)
    print(complex_num_1_object.r, complex_num_1_object.i)