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
########################
# Решение задачи 26.1 'Управление очередью':
queue = ["John", "James", "Amy"]
txt = input()
queue.append(txt)
print(queue)
########################
########################
# Решение задачи 26.2 'Средний элемент':
items = [2, 4, 6, 8, 10, 12, 14]
print(len(items) // 2)
########################
########################
# Решение задачи 26.4 'Минимум и Максимум':
numbers = [14, 5, 6, 8, 17, 28]
print(min(numbers)+max(numbers))
########################
########################
# Решение задачи 27.1 'Четные числа':
x = 0
while x <= 10:
    if (x % 2) == 0:
        print(x)
    x += 1
########################
########################
# Решение задачи 27.2 'Сумма цифр':
n = int(input())
length = 0
while n > 0:
    length += n % 10
    n //= 10
print(length)
########################
########################
# Решение задачи 27.3 'Бесконечные циклы':
items = []
while True:
    n = int(input())
    if n != 0:
        items.append(n)
    elif n == 0:
        break
print(items)
########################
########################
# Решение задачи 27.4 'Сегодня акция!':
items = [23, 555, 666, 123, 128, 4242, 990]
sum = 0
n = 0
while n < len(items):
    num = items[n]
    n += 1
    if num % 2 != 0:
        continue
    sum += num
print(sum)
########################
########################
# Решение задачи 28.3 'Итерация':
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sum = 0
for x in list:
    sum += x
print(sum)
########################
########################
# Решение задачи 29.4 'Выбор даты':
a = int(input())
b = int(input())
date = list(range(a, b))
print(date)
########################
########################
# Решение задачи 31 'FizzBuzz':
n = int(input())
for x in range(1, n):
    if x % 2 == 0:
        print()
    elif x % 3 == 0 and x % 5 == 0:
        print("SoloLearn")
    elif x % 3 == 0:
        print("Solo")
    elif x % 5 == 0:
        print("Learn")
    else:
        print(x)
########################
