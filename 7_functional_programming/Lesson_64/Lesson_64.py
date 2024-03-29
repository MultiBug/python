####################################
# 64.1 Функциональное программирование
def apply_twice(func, arg):
    return func(func(arg))
def add_five(x):
    return x + 5
print(apply_twice(add_five, 10))
####################################
####################################
# 64.2 Чистые функции
#Чистая функция:
def pure_function(x, y):
  temp = x + 2*y
  return temp / (2*x + y)
#Нечистая функция:
some_list = []
def impure(arg):
  some_list.append(arg)
####################################
####################################
# 64.3 Чистые функции
####################################
