numbers = [108, 389, 28, 0, 100, 14, 3829,							 99029, -1, 94, 1, 7, 837, 22, 101]
max_n = numbers.index(max(numbers))
min_n = numbers.index(min(numbers))
numbers[max_n], numbers[min_n] = numbers[min_n], numbers[max_n]
print(numbers)