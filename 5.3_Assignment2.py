# Programming for Everybody. Getting started with Python
# Santiago Botero S.
# E-mail: sboteros@unal.edu.co
# Date: 22/01/2020
# Encoding: UTF-8

# # 3.3 Write a program to prompt for a score between 0.0 and 1.0. If the score
# is out of range, print an error. If the score is between 0.0 and 1.0, print a
# grade using the following table: Score Grade >= 0.9 A >= 0.8 B >= 0.7 C >= 0.6
# D < 0.6 F If the user enters a value out of range, print a suitable error
# message and exit. For the test, enter a score of 0.85.

score = input('Enter score:')
try :
    score = float(score)
except :
    score = -1

if not (score >= 0 and score <= 1) :
    print('Bad score')
elif score >= 0.9 :
    print('A')
elif score >= 0.8 :
    print('B')
elif score >= 0.7 :
    print('C')
elif score >= 0.6 :
    print('D')
else :
    print('F')
