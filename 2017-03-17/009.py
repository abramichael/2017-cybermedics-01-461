def our_int(s):
	n = 0
	for cd in s:
		digit = ord(cd) - ord('0')
		n = n * 10 + digit
	return n
	
	
def our_range(n):
	lst = []
	i = 0
	while i < n:
		lst.append(i)
		i += 1
	return lst
	
	
x = our_int(raw_input())
print x * 2


for i in our_range(1000):
	print i