# Задача 8: 
# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками 
# (то есть разломить шоколадку на два прямоугольника).
# 3 2 4 -> yes
# 3 2 1 -> no

# width = int(input())
# length = int(input())
# slice = int(input())
# if slice < width * length and (slice % width == 0 or slice % length == 0): print('yes')
# else: print('no')

# Решение преподавателя
n = int(input())
m = int(input())
k = int(input())

if (k % n == 0 or k % m == 0) and k < m * n:
    print ("YES")
else: print ("NO")