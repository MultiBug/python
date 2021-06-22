####################################
# 67.1 Генераторы
def countdown():
    i=5
    while i > 0:
        yield i
        i -= 1
for i in countdown():
    print(i)
####################################
####################################
# 67.2 Генераторы
def infinite_sevens():
  while True:
    yield 7
for i in infinite_sevens():
  print(i)
####################################
####################################
# 67.3 Генераторы
def numbers(x):
    for i in range(x):
        if i % 2 == 0:
            yield i
print(list(numbers(11)))
####################################
