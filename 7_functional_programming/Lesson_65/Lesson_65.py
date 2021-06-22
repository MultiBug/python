####################################
# 65.1 Функция lambda
def my_func(f, arg):
    return f(arg)


my_func(lambda x: 2*x*x, 5)
####################################
####################################
# 65.2 Функция lambda
#named function
def polynomial(x):
    return x**2 + 5*x + 4
print(polynomial(-4))
#lambda
print((lambda x: x**2 + 5*x + 4) (-4))
####################################
####################################
# 65.3 Функция lambda
double = lambda x: x * 2
print(double(7))
####################################
