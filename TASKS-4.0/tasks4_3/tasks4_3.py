file = open("guest_book.txt", "a")

while True:
	guest_name = input("Если вы хотите выйти введите 'exit'\nВведите ваше имя: ")
	if guest_name.lower() == "exit":
		break
	file.write(f"Приветствуем вас в нашем отеле, {guest_name}\n")
file.close()

file_2 = open("guest_book.txt")
print(file_2.read())
file_2.close()		
		

