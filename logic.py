import sys
import os
import math
import string



sys.stdin = open("logicgates/logicgates.dat", "r")


#basic or logic gate!

def or_gate(a, b):
	if a == 1 or b == 1:
		return 1
	return 0 


#basic and logic gate!
def and_gate(a, b): 
	if a == 1 and b == 1:
		return 1
	return 0 


#basic not logic gate!
def not_gate(a):
	if a == 1:
		return 0
	return 1 


#calling both not function first, then or function

#fucked up codes

try:
	a = int(input("O or 1? "))

except EOFError:
    	print ("Error: No input or End Of File is reached!")
    