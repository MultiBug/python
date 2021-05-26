########################
# Решение задачи 20.2 'Мороженое для всех!':
money = int(input())
price = int(input())
x = price*10
if money <= money + price:
    if money >= x:
        y = money % x
    print(y)
########################
