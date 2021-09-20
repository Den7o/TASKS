weight = int(input("Введите ваш вес: "))
number = 0
while number <= 15:
	number += 1
	print(f"{number} год: {weight*0.165}кг")
	weight += 1