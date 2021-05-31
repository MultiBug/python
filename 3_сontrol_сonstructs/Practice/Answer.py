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
########################
# Решение задачи 22.1 'Магазин закрыт!':
hour = int(input())
day = int(input())
if (hour >= 10 and hour <= 21) and (day >=1 and day <= 5):
    print('Open')
elif (hour < 10 and hour > 21) or (day >= 6 or day <= 0):
    print('Closed')
########################
########################
# Решение задачи 22.3 'Возрастные группы':
age = int(input())
if (age >= 0 and age <=11):
    print('Child')
elif (age >= 12 and age <=17):
    print('Teen')
elif (age >= 18 and age <=64):
    print('Adult')
elif age >= 65:
    print('Senior')
########################
########################
# Решение задачи 23.2 'Скидка на обучение':
sem1_score = int(input())
sem2_score = int(input())
avg = int((sem1_score + sem2_score) // 2)
if (avg >= 90 and avg <= 100):
    print(50)
elif (avg >= 80 and avg <= 89):
    print(30)
elif (avg >= 70 and avg <= 79):
    print(10)
elif (avg >= 0 and avg <= 69):
    print(0)
########################
########################
# Решение задачи 24.2 'Автомат с фруктами':
fruits = ["apple", "cherry", "banana", "kiwi", "lemon", "pear", "peach", "avocado"]
n = int(input())
if n == 0:
    print(fruits[0])
elif n == 1:
    print(fruits[1])
elif n == 2:
    print(fruits[2])
elif n == 3:
    print(fruits[3])
elif n == 4:
    print(fruits[4])
elif n == 5:
    print(fruits[5])
elif n == 6:
    print(fruits[6])
elif n == 7:
    print(fruits[7])
elif (n < 0 or  n > 7):
    print('Wrong number')
########################
########################
# Решение задачи 24.4 'Каждый третий знак':
text = input()
print(text[2])
########################
########################
# Решение задачи 25.2 'Операции со спискoм':
items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num = int(input())
items[num] = 'x'
print(items)
########################
########################
# Решение задачи 25.3.1 'Создаем поисковый механизм':
s = input()
if 'a' in s:
    print("Match")
else:
    print("No match")
########################
########################
# Решение задачи 25.3.2 'Бинго!':
items = [42, 88, 721, 12, 43, 22, 908]
num = int(input())
if num in items:
    print('bingo')
else:
    print()
########################
