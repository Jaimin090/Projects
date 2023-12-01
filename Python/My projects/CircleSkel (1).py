# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 02:46:42 2022

@author: amoussa
"""
import math
class Circle():
    __nbr_of_circles = 0
    def __init__ (self, radius):
        self.__radius = radius
        Circle.__nbr_of_circles += 1

    def area (self):
        return math.pi * (self.__radius ** 2)
    
    def perimeter (self):
        return 2 * math.pi * self.__radius
    
    def get_nbr_of_circles ():
        return Circle.__nbr_of_circles
    
    
def main():
    circle1 = Circle(8)
    print('Circle 1')
    print(f"\tArea      = {circle1.area():.4f}" )
    print(f"\tPerimeter = {circle1.perimeter():.4f}")
    circle2 = Circle(5)
    print('Circle 2')
    print(f"\tArea      = {circle2.area():.4f}")
    print(f"\tPerimeter = {circle2.perimeter():.4f}")
    print(f"Number of circles = {Circle.get_nbr_of_circles()}")

if __name__ == '__main__':
    main()

