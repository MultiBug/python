########################
# Решение задачи 43.3 'Система ПИН-кодов банковский карт':
pin = input()
try:
    pin = int(pin)
    print("PIN code is created")
except ValueError:
    print("Please enter a number")
########################
########################
# Решение задачи 44.2 'Готовим кофе':
coffee = ["Café Latte", "Caffe Americano", "Espresso", "Cappuccino", "Macchiato"]

choice = int(input())

try:
    print(coffee[choice])

except IndexError:
    print('Invalid number')

finally:
    print("Have a good day")
########################
########################
# Решение задачи 48.2 'Держим себя в форме': 
file = open("/usercode/files/pull_ups.txt", 'r+')
n = int(input())
lines = file.readlines()
print(lines[n])
file.close()
########################
########################
# Решение задачи 49.2 'С новой строки':
names = ["John", "Oscar", "Jacob"]
file = open("names.txt", "w+")
print(names[0])
print(names[1])
print(names[2])
file.close()
file = open("names.txt", "r")
file.close()
########################
########################
# Решение задачи 52 'Заголовки книг':
file = open("/usercode/files/books.txt", "r")
for line in file:
    print(line[0]+str(len(line) - line.count('\n')))
file.close()
########################
