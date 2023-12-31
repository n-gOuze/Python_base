# Задача 10. 
# На столе лежат n монеток. 
# Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть.

# Пример:
# 5 -> 1 0 1 1 0
# 2

# План решения:
# Ввод пользователем количества монет
# Генерация двузначного (0,1) массива с длиной = количеству монет
# Подсчет количества монет орлом (1)
# Подсчет количества монет решкой (0)
# Сравнение количества орлов и решки = минимальное количество монет

number = int(input('Введите количество монет: '))
from random import randint
count = 0
min_count = 0
for i in range(0, number, 1):
    coins = randint(0, 1)
    print(coins)
    if coins == 0:
        count += 1
    if coins == 1:
        min_count += 1
        if count <= min_count:
            min_count = count
print(f'Минимальное количество монет: {min_count}')

# Решение преподавателя 1

n = int(input())
count_one = count_zero = 0

for i in range(n):
    coin = int(input())
    if coin:
        count_one += 1
    else: 
        count_zero += 1

if count_one > count_zero:
    print(count_zero)
else:
    print(count_one)

# Решение преподавателя 2

n = int(input())
count = 0

for i in range(n):
    if int(input()):
        count += 1

print (min(count, n - count))