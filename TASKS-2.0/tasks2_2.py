a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
b = [-1, 5, 10, 9, 4, 921, 1]
y = []
for x in a:
	for z in b:
		if x == z:
			y.append(x)
print(y)