# Срезы кортежей
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(numbers[2:5])   # (3, 4, 5)
print(numbers[:4])    # (1, 2, 3, 4)
print(numbers[5:])    # (6, 7, 8, 9)
print(numbers[::2])   # (1, 3, 5, 7, 9)
print(numbers[::-1])  # (9, 8, 7, 6, 5, 4, 3, 2, 1)