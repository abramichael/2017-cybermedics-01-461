#file without extention
filename = raw_input()
n = input()

for k in range(n):
	f = open(filename + ".txt")
	g = open(filename + "-copy-%s.txt" % k , "w")
	g.write(f.read())
	g.close()
	f.close()
