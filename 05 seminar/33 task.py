# Задача №33. 
# Хакер Василий получил доступ к классному журналу и 
# хочет заменить все свои минимальные оценки на максимальные. 
# Напишите программу, которая заменяет оценки Василия, но наоборот: 
# все максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

print(list(map(int, input().split()))) # зашла строка - input, мы её разбили split
# функция map применит int на каждый элемент списка и сделает целочисленным
# list - преобразовывает значения в список

numbers = list(map(int, input().split()))
max_l = max(numbers)
min_l = min(numbers)
result = [i if i != max_l else min_l for i in numbers]
print(result)