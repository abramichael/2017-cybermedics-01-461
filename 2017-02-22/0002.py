# e^x

x = float(raw_input())

a = 1.0
s = a

eps = 0.000000001
n = 1
while (abs(a) > eps):
	print(s)
	a = x * a / n
	s += a
	n += 1

print(s)
