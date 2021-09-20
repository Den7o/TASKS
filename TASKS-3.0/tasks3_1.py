words = input("Введите слова: ").split()
words.sort(key = lambda long: len(long)) 
print(f"Рузультат: {words}")
