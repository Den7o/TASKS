texts = input("Введите сообщение: ")

upper_text = 0
lower_text = 0

for text in texts:
	if text.islower():
			lower_text+=1 
	else:
		upper_text+=1
len_text = len(texts)

print(f"Процента мальеньких букв: {lower_text*100/len_text}")
print(f"Проценты больших букв: {upper_text*100/len_text}")