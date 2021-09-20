numbers = [0]
numbers_with_one = numbers*100
numbers_with_one[0] = numbers_with_one[-1] = 1
print(numbers_with_one)