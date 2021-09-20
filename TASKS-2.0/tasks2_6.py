number = int(input("Введите число:  "))
number = list(range(1,number+1))
multiplication = 1
for a in number:
	multiplication *= a
print(f"Число n!:  {multiplication}")