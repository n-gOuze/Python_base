# Задача №19. 
# Дана последовательность из N целых чисел и число K. 
# Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо, 
# K – положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

list_nums = [1, 2, 3, 4, 5]
k = 1

print(list_nums)

for i in range(k): # переставляем k раз
    list_nums.insert(0, list_nums.pop(-1)) # insert - добавляет новый элемент в любое место списка. 
# Метод принимает два параметра: индекс по которому будет вставлен элемент и сам элемент.
# pop - удаляет элемент с -1 индекса и ставит его на 0 индекс

print(list_nums)

