#!/usr/bin/env python3.7

# Python implementation here
fahrenheit = float(input("What temperature (in Fahrenheit) would you like converted to Celsius? "))
celsius = (fahrenheit - 32) * 5 / 9

#The output will be like this: ... F is ... C
print(fahrenheit,"F is", round(celsius, 2),"C", sep=" ")