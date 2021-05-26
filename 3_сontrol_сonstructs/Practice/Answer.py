########################
# Решение задачи 20.2 'Мороженое для всех!':
money = int(input())
price = int(input())
x = price*10
y = money%x
if money >= x:
    print(y)
if money < x:
    print()
########################
