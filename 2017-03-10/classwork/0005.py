n = int(raw_input())
m = int(raw_input())
s = 0
for i in xrange(1, n + 1):
	p = 1
	for j in xrange(1, m + 1):
		p *= i * j 
	s += p
print(s)