#file without extention
filename = raw_input()
n = input()

for k in range(n):
	f = open(filename + ".txt")
	g = open(filename + "-copy-%s.txt" % k , "w")
	for line in f:
		g.write(line)
	g.close()
	f.close()
