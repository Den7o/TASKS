files = open("text.txt")
files = files.readlines()
number = 0

print(f"Всего: {len(files)} строк\n")
for file in files:
	file = file.strip("\n")
	
	while True:	
		number += 1
		file_2 = file.split()
		print(f"В {number} строке: {len(file)} символов и {len(file_2)} слов")
		break
