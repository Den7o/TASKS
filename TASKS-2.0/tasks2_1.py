time1 = input("Введите время: ")
time2 = input("Введите время: ")

the_1_numbers = time1.replace(":", " ").split()
the_2_numbers = time2.replace(":", " ").split()

calculation_1 = int(the_1_numbers[0])*3600 + int(the_1_numbers[1])*60 + int(the_1_numbers[2])
calculation_2= int(the_2_numbers[0])*3600 + int(the_2_numbers[1])*60 + int(the_2_numbers[2])

if calculation_1 <= calculation_2:
	print(f"{calculation_2 - calculation_1} секунд разница")
	
else:
	print("Первая отметка должна быть раньше по времени чем вторая!")