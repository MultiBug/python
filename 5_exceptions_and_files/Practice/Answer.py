########################
# Решение задачи 43.3 'Система ПИН-кодов банковский карт':
pin = input()
try:
    pin = int(pin)
    print("PIN code is created")
except ValueError:
    print("Please enter a number")
########################
