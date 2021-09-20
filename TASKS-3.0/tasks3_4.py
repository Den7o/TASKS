age = int(input("Введите ваш возраст: "))
if age%2 == 0:
	for number in range(0, age+1, 2):
		print(number)
else:
	for number2 in range(1, age+1, 2):
		print(number2)