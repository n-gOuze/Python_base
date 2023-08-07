# Задача 14. 
# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
# Пример:
# 10 -> 1 2 4 8

number = int(input('Введите число N: '))
power = 1
while power < number / 2:
    power = power * 2
    print(power)
# при таком решении нулевой степени не получается

# Решение преподавателя

n = int(input())
pow_two = 1

while pow_two <= n:
    print(pow_two, end=" ")
    pow_two *= 2