# Задача №29. 
# Ваня и Петя поспорили, кто быстрее решит следующую задачу: 
# “Задана последовательность неотрицательных целых чисел. 
# Требуется определить значение наибольшего элемента последовательности, 
# которая завершается первым встретившимся нулем (число 0 не входит в последовательность)”. 
# Однако 2 друга оказались не такими смышлеными. 
# Никто из ребят не смог до конца сделать это задание. 
# Они решили так: у кого будет меньше ошибок в коде, тот и выиграл спор. 
# За помощью товарищи обратились к Вам, студентам.

# Ваня
n = int(input())
max_number = 1000 # заменить на n
while n != 0:
 n = int(input())
 if max_number > n: # заменить на <
 max_number = n # исправить отступ
print(max_number)

# Петя
n = int(input())
max_number = -1 # исправить на n
while n < 0: # исправить на !=0
 n = int(input())
 if max_number < n: 
 n = max_number # исправить отступ и поменять местами
print(n) # исправить на max_number