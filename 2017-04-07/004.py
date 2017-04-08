f = open("mkb10.txt")

prev = 'A'
g = open('mkb10-%s.txt' % prev, "w")

for line in f:
	#lst = line.split("\t")
	#c = lst[1][0]
	c = line.split("\t")[1][0]
	if (c != prev):
		g.close()
		g = open('mkb10-%s.txt' % c, "w")
	prev = c
	g.write(line)

f.close()