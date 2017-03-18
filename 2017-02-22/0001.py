import time

x = float(raw_input())
c1 = time.time() * 1000000000
print time.time()
y = 2 * x ** 4 - 3 * x ** 3 + 4 * x ** 2 - 5 * x + 6
c2 = time.time() * 1000000000
print time.time()
print("TIME:", (c2 - c1))
print(y)