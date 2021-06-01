items = [23, 555, 666, 123, 128, 4242, 990]
sum = 0
n = 0
while n < len(items):
    num = items[n]
    n += 1
    if num % 2 != 0:
        continue
    sum += n
print(sum)