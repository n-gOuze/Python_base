# Задача №27. 
# Пользователь вводит текст(строка). 
# Словом считается последовательность непробельных символов идущих подряд, 
# слова разделены одним или большим числом пробелов. 
# Определите, сколько различных слов содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells
# Output: 13

text = input('Введите текст: ').upper() # подготавливаем текст - приводим к одному регистру
print('Количество различных слов в тексте: ', len(set(text.split())))
# split - разбиваем слова по пробелам
# set - убирает дубликаты
# len - считаем, сколько элементов осталось
