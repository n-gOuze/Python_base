# Задача №43. 
# Дан список чисел. 
# Посчитайте, сколько в нем пар элементов, равных друг другу. 
# Считается, что любые два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список чисел. 
# Все числа списка находятся на разных строках.
# Ввод:
# 1 2 3 2 3 
# Вывод:
# 2

list_n = [int(input()) for i in range int(input)]
# set_n = list(set(list_n))
# list_m = print(sum([list_n.count(set_n[i])//2 for i in range(len(set_n))]))

count = [list_n[i] for i in range(len(list_n)) for j in range(i + 1, len(list_n)) if list_n[j] == list_n[i]]
print(count, len(count))
