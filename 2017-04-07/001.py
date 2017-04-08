f = open("mkb10.txt")
g = open("mkb10-copy.txt", "w")

for line in f:
	g.write(line)

f.close()
g.close()

