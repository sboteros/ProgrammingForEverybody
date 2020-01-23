# Programming for Everybody. Getting started with Python
# Santiago Botero S.
# E-mail: sboteros@unal.edu.co
# Date: 22/01/2020
# Encoding: UTF-8

# 3.1 Write a program to prompt the user for hours and rate per hour using input
# to compute gross pay. Pay the hourly rate for the hours up to 40 and 1.5 times
# the hourly rate for all hours worked above 40 hours. Use 45 hours and a rate
# of 10.50 per hour to test the program (the pay should be 498.75). You should
# use input to read a string and float() to convert the string to a number. Do
# not worry about error checking the user input - assume the user types numbers
# properly.

hours = input('Enter hours:')
hours = float(hours)
rate = input('Enter rate:')
rate = float(rate)

if hours > 40 :
    pay = (rate * 40) + (1.5 * rate * (hours - 40))
else :
    pay = rate * hours

print('Pay:', pay)
