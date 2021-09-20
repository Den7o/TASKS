files = open("text.txt")
files = files.readlines()
a = []
b = []
for file in files:
	for letters in file:
		a.append(letters)
	file = file.split()
	for words in file:
		b.append(words)
print(f"Процент символов в тексте: {a.count('а')*100/len(a)}%\n")
print(f"Процент слов в тексте: {b.count('но')*100/len(b)}%")

