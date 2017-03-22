#import random
from random import randrange as rand

def sum(a, b):
	c = a + b
	return c

def check_if_exists(list_of_elements, ideal_element):
	for elem in list_of_elements:
		if ideal_element == elem:
			return True
	return False

def create_random_list(n, ratio):
	lst = []
	for i in range(n):
		lst.append(rand(ratio))
	return lst


#lst = create_random_list(40, 100)
#print lst
#ideal = rand(100)
#print ideal

#print check_if_exists(lst, ideal)