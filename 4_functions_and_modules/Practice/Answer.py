########################
# Решение задачи 33.2 'Добро пожаловать в SoloLearn, username':
def welcome_message():
    name = input()
    print("Welcome,", name)
welcome_message()
########################
########################
# Решение задачи 34.2 'Совпадение паролей':
password = input()
repeat = input()
def validate(password, repeat):
    if password == repeat:
        print('Correct')
    else:
        print('Wrong')
validate(password, repeat)
########################
########################
# Решение задачи 34.3 'Площадь прямоугольника':
length = int(input())
width = int(input())
def area(length, width):
    print(int(length) * int(width))
    if length == width:
        print('Square')
area(length, width)
########################
