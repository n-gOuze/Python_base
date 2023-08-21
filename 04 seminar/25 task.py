# Задача №25. 
# Напишите программу, которая принимает на вход строку, и отслеживает, 
# сколько раз каждый символ уже встречался. 
# Количество повторов добавляется к символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию .split()

# string = "a a a b c a a d c d d".split() # split превращает строку в список

# for i in range(1, len(string)):
#     string[i] += f"_{string[0:i-1].count(string[i])}"

# print(*string)

string = "a a a b c a a d c d d".split()

dict = {}.fromkeys(string, 0)

for i in string:
    print(f"{i}_{dict[i]}" if dict[i] else i, end=" ") # тернарный оператор: в центре логиечское выражение,
    # слева - если истина, справа - если ложно
    # if dict[i] != 0:
    #     print(f"{i}_dict{i}")
    # else:
    #     print(i, end=" ")
    dict[i] += 1

