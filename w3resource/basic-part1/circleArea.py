"""
    4. Write a Python program that calculates the area of a circle based on the radius entered by the user.
    Sample Output :
    r = 1.1
    Area = 3.8013271108436504
"""

import math

def areaCircle():
    r = float(input("Insert the radius of the circle: "))
    
    area = (r**r)*math.pi
    print("Radius is: " + str(r))
    print("Area of the circle is: " + str(area))


areaCircle()
