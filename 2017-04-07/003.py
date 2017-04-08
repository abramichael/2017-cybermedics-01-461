import time
f = open("mkb10.txt")

c = 'D'

g = open("mkb10-%s.txt" % c, "w")

t = time.time()

for line in f:
	lst = line.split("\t")
	ident = lst[1]
	if ident[0] == c:
		g.write(line)

print time.time() - t

f.close()
g.close()
