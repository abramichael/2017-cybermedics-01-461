a = float(raw_input("a = "))
b = float(raw_input("b = "))
c = float(raw_input("c = "))
D = b * b - 4 * a * c
if D == 0:
	n = 1
elif D > 0:
	n = 2
else: 
	n = 0
print("%s roots" % n)