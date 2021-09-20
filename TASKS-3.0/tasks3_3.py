class_a = int(input("Введите кол-во студентов в A классе: "))
class_b = int(input("Введите кол-во студентов в B классе: "))
class_c = int(input("Введите кол-во студентов в C классе: "))

chairs_for_a = class_a // 1.9
chairs_for_b = class_b // 1.9
chairs_for_c = class_c // 1.9
max_chairs = chairs_for_a + chairs_for_b + chairs_for_c

print(f"\nДля А класса нужно: {chairs_for_a} стульев. \nДля B класса нужно: {chairs_for_b} стульев. \nДля С класса нужно: {chairs_for_c} стульев.\nДля трех классов понадобится: {max_chairs} стульев.")