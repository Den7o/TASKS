massage = input("Введите 'Привет', чтобы начать работу: ")

if massage.lower() == "привет":
	print("\nСписок офисов: \n1)Kazakstan\n2)Paris\n3)Uar\n4)Kyrgystan\n5)San_Francisco\n6)Germany\n7)Moscow\n8)Sweden")
	text = input("\nВыберите офис, в который вы хотите отправить жалобу: ")

	if text.lower() == "kazakstan" or text.lower() == "paris" or text.lower() == "uar" or text.lower() == "kyrgystan" or text.lower() == "san_francisco" or text.lower() == "germany" or text.lower() == "moscow" or text.lower() == "sweden":
		complaint = input("Введите жалобу: ")
		file = open(f"google_{text.lower()}.txt", "w")
		file.write(complaint)
		file.close()
	
	else:
		print("Вы не ввели офис, в который хотите отправить жалобу.")