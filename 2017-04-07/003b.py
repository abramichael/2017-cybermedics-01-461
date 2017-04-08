import time
f = open("mkb10.txt")

c = 'D'

g = open("mkb10-%s.txt" % c, "w")

s = 0
t = time.time()

for line in f:
	lst = line.split("\t")
	ident = lst[1]
	if ident[0] == c:
		s = 1
		g.write(line)
	else:
		if (s == 1):
			break

print time.time() - t

f.close()
g.close()
