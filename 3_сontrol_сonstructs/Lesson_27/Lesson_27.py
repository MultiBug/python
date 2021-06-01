####################################
# 27.1 Циклы while
i = 1
while i <= 5:
    print(i)
i = i + 1
print("Finished!")
####################################
####################################
# 27.2 Циклы while
x = 1
while x < 10:
    if x % 2 == 0:
        print(str(x) + " is even")
    else:
        print(str(x) + " is odd")
x += 1
####################################
# 27.3 Циклы while
i = 0
while True:
    print(i)
    i = i + 1
    if i >= 5:
        print("Breaking")
        break
print("Finished")
####################################
# 27.4 Оператор continue
i = 1
while i <= 5:
  print(i)
  i += 1
  if i == 3:
    print("Skipping 3")
    continue
####################################
