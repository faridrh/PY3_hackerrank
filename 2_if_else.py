'''
Task
Given an integer, , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of 2 to 5, print Not Weird
If  is even and in the inclusive range of 6 to 20, print Weird
If  is even and greater than 20, print Not Weird

Input Format

A single line containing a positive integer, .

Constraints

Output Format

Print Weird if the number is weird. Otherwise, print Not Weird.

'''

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    def even(number):
        if number %2 ==0:
            return True
        else:
            return False
    if even(n) and (n<=5) and (n>=2):
        print("Not Weird")
    if even(n) and (n<=20) and (n>=6):
        print("Weird")
    if even(n) and (n>20):
        print("Not Weird")
    if even(n) is False:
        print ("Weird")
