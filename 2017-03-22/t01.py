#import random
from random import randrange as rand

n = 40

ideal = rand(100)
lst = []
for i in range(n):
	lst.append(rand(100))

print ideal
print lst

found = False
i = 0
while (i < n and not found):
	if lst[i] == ideal:
		found = True
	i += 1

print "Found: %s" % found