import random

lst = []

n = int(input())
for i in range(n):
	#lst.append(i)
	lst.append(randrange(n))

# ...

max = lst[0]
for x in lst:
	if max < x:
		max = x

print max