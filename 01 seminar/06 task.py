# Задача 6: 
# Вы пользуетесь общественным транспортом? 
# Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.

# ticket = int(input())
# first_sum = (ticket % 1000 // 100 +
#              ticket % 100 // 10 +
#              ticket % 10)
# second_sum = (ticket % 1000000 // 100000 + 
#               ticket % 100000 // 10000 + 
#               ticket % 10000 // 1000)
# if first_sum == second_sum : print('yes')
# else: print('no')

# Решение циклом
ticket = int(input())
sum_first = 0
sum_last = 0

while ticket:
    digit = ticket % 10
    if ticket > 999:
        sum_first += digit
    else:
        sum_last += digit
    ticket //= 10
print (f"Счастливый билет {sum_first == sum_last}")

# Решение по индексам
# ticket = int(input())
# sum_first = int(ticket[0]) + int(ticket[1]) + int(ticket[2])
# sum_last = int(ticket[3]) + int(ticket[4]) + int(ticket[5])
# print (f"Счастливый билет {sum_first == sum_last}")
