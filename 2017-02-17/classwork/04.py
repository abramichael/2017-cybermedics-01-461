x = float(raw_input())
y = float(raw_input())
z = float(raw_input())
# s = (x + y + z) / y - (z + y)/(z + 2)
# print(s)
x += y # x = x + y
x += z # x = x + z 
x /= y # x = x / y 
y += z # y = y + z
z += 2 # z = z + 2
y /= z # y = y / z
x -= z # x = x - z   
print(x)