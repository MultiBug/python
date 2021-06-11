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
# Решение задачи 48.4 'С новой строки':
names = ["John", "Oscar", "Jacob"]
file = open("names.txt", "w+")
print(names[0])
print(names[1])
print(names[2])
file.close()
file = open("names.txt", "r")
file.close()
########################
