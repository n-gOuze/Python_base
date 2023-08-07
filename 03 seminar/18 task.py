# # Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент 
# к заданному числу X. Пользователь в первой строке вводит натуральное 
# число N – количество элементов в массиве. 
# # В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X.
# # Пример:
# # 4
# # 1 2 4 5
# # 3
# # -> 2

# Решение преподавателя 1

from random import randint

list_nums = [randint(1, 21) for _ in range(int(input()))]

print(list_nums)
num = int(input())
right_num = list_nums[0]

for i in list_nums: # в данном случае пробегается по значениям содержимого
    # если б было for i in range, то по индексам
    if abs(num - i) < abs(num - right_num): # вычитаем из нашего числа значения и смотрим наименьшее отклонение
        right_num = i

print(right_num)

# Решение преподавателя 2

from random import randint

n = int(input())
list_nums = [randint(1, 50) for _ in range(n)]

print(list_nums)

b = int(input())
m = min(list_nums, key=lambda x: abs(x - b))

print(m)