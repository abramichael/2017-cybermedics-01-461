a = float(raw_input("a = "))
b = float(raw_input("b = "))
c = float(raw_input("c = "))
D = b * b - 4 * a * c
if D == 0:
	x = -1 * b / (2 * a)
	print("1 roots: %s" % x) 
elif D > 0:
	x1 = (-1 * b - D ** 0.5) / (2 * a)
	x2 = (-1 * b + D ** 0.5) / (2 * a)
	print("2 roots: %s, %s" % (x1, x2)) 
else:
	print("0 roots")
