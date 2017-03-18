n = int(input())

a = []
for i in range(n):
	a.append(float(input()))

b = []
for i in range(n):
	b.append(float(input()))

s = 0
for i in range(n):
	s += a[i] * b[i]

len_a = 0
for x in a:
	len_a += x * x
len_a = len_a ** 0.5

len_b = 0
for x in b:
	len_b += x * x
len_b = len_b ** 0.5

cos_ab = s/(len_a * len_b)
print(cos_ab)