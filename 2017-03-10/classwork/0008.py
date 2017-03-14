n = int(raw_input())
m = int(raw_input())
s = 0
for i in xrange(1, n + 1):
	
	s2 = 0
	for j in xrange(1, m + 1):
		s2 += j 
	s += s2 * i 

print(s)