# small letter by capital letter

c = raw_input()

# check if small letter
while not('a' <= c <= 'z'):
	c = raw_input("Not a small letter. Try again\n")
	
distance = ord('a') - ord('A')
n = ord(c) - distance
print(chr(n))
