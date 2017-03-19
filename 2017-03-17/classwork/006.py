# coding: utf-8

import random
c = 100
x = random.randrange(c)

n = input("Enter number (0-%s): " % c)
while (n != x):
	if (n > x):
		print("<")
	else:
		print(">")
	n = input("Enter number: ")

print("URA!")