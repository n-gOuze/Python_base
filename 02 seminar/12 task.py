# Задача 12.
# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
# Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.

# План решения:
# Сумма чисел и произведение чисел не могут быть больше самого числа.
# Соответственно, они являются лимитом для перебора чисел.
# Пользователь вводит число суммы и число произведения.
# Устанавливаем флажок True
# Для Х в диапазоне суммы проверяем:
# если х умноженный на разницу между суммой и х равен произведению, то
# печатаем два числа: Х и разницу между суммой и Х
# если нет - флажок False и завершаем цикл
# Если результат не найден печатаем No results

# Решение преподавателя 1
# Теорема Виета

from time import time # просто добавлено для подсчета времени решения

# 1_000_000_001 1_000_000_000
s = int(input("Сумма чисел: "))
p = int(input("Произведение чисел: "))
answer = "Я не знаю"

start = time()

d = s ** 2 - 4 * p # дискриминант

if d >= 0:
    x_1 = (s + d ** 0.5) // 2
    x_2 = (s - d ** 0.5) // 2
    if x_1 * x_2 == p:
        answer = f"{x_1}, {x_2}"

print(answer)
print (time() - start)

# Решение преподавателя 2

s = int(input())
p = int(input())

for num_1 in range(1, p):
    num_2 = s - num_1
    if s == num_1 + num_2 and p == num_2 * num_1:
        print(num_1, num_2)
        break