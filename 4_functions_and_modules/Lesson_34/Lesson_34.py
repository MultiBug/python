####################################
# 34.1 Аргументы
def print_with_exclamation(word):
    print(word + "!")
print_with_exclamation("spam")
print_with_exclamation("eggs")
print_with_exclamation("python")
####################################
####################################
# 34.2 Параметры
def print_sum_twice(x,y):
    print(x + y)
    print(x + y)
print_sum_twice(5, 8)
####################################
####################################
# 34.3 Аргументы
def function(variable):
    variable += 1
    print(variable)
    function(7)
print(variable)
####################################
