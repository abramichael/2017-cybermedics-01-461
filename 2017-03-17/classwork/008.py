s = raw_input()

#x = int(s)
n = 0
for cd in s:
	digit = ord(cd) - ord('0')
	n = n * 10 + digit
	

	