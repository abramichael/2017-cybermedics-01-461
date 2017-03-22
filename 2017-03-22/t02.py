#import random
from random import randrange as rand

n = 40

ideal = rand(100)
lst = []
for i in range(n):
	lst.append(rand(100))

print ideal
print lst

k = 0
for x in lst:
	if x == ideal:
		print "Found"
		k = 1
		break

if k == 0:
	print "Not Found"