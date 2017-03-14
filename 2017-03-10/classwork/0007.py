n = int(raw_input())
m = int(raw_input())
s = 0
i = 1
while i <= n:
	s2 = 0
	j = 1
	
	while (j <= m):
		s2 += i * j
		j += 1

	s += s2
	i += 1
