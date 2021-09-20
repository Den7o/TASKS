files =  open("text.txt")
files = files.readlines()
number = 0
for file in files:
	grade = file.strip("\n")
	grade = int(grade[-1])
	number += grade
	if grade <= 3:
		print(file.strip())
print(f"Средний балл: {number/len(files)}")