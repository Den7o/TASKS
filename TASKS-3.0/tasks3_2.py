apple = int(input("Введите кол-во яблок: "))
students = int(input("Введите кол-во студентов: "))

if students > apple:
	print("Яблок меньше чем учеников,так что никто не получит яблок")

else:
	get_apple = apple//students
	remainder = apple - get_apple * students
	print(f"Каждый студент получит: {get_apple} яблок")
	print(f"В корзине осталось: {remainder} яблок")