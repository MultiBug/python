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
########################
# Решение задачи 21.1 'Вышибала в ночном клубе':
age = int(input())
name = input()
if age >= 18:
    print('Welcome ' + name)
else:
    print('Sorry')
########################
########################
# Решение задачи 21.2 'Пифагор или нет?':
side1 = int(input())
side2 = int(input())
side3 = int(input())
if (side3**2) == (side1**2) + (side2**2):
    print("Right-angled")
else:
    print("Not right-angled")
########################
########################
# Решение задачи 21.3.1 'Робот, который любит порядок':
color = input()
if color == 'red':
    print(1)
elif color == 'green':
    print(2)
elif color == 'black':
    print(3)
########################
########################
# Решение задачи 21.3.2 'Учитывая четность':
number = input()
if (int(number) % 2) == 0:
    print(int(number)*2)
elif (int(number) % 2) != 0:
    print(int(number)*3)
elif int(number) == 0:
    print(0)
########################
