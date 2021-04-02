print("www.sololearn.com")
print('\n')
"""
module 1
"""
print('========== Module 1: Basics ==========')
print('Hello world!')
print('--------------------')
print('Многострочный \nвывод строки \nс переносом')
print('--------------------')
print('float 3/4 = ' + str(3 / 4))
print('float ' + str(0.42))
print('Возведение в степень 2^5 = ' + str(2 ** 5))
print('Возведение в степень 9^0.5 = ' + str(9 ** (1 / 2)))
print('Целочисленное деление 20//6 = ' + str(20 // 6))
print('Целочисленное деление 20//6 = ' + str(20 // 6))
print('Деление по модулю 20%6 = ' + str(20 % 6))
print('Деление по модулю (float) 1.25%0.5 = ' + str(1.25 % 0.5))
print('\n')
"""
module 2
"""
print('========== Module 2: Strings & Variables ==========')
print('Вывод в разных ковычках:')
print("\"Python is fun!\"")
print('\'Python is fun!\'')
print('Экранирование:')
print('\'Brian\'s mother: He\'s not an angel. He\'s a very naughty boy!\'')
print("\"Brian\'s mother: He\'s not an angel. He\'s a very naughty boy!\"")
print('\n')
print("""this 
is a 
multiline text""")
print("Spam" + ' eggs')
print("2" + " 2")
print("spam " * 3)
print(4*'2 ')
print('user = \"James\"')
print('this_is_a_normal_name = 7')
print('123abc = 7 SyntaxError: invalid syntax')
x = 7
print(x)
print(x+3)
x = 123.456
print(x)
x = "This is a string"
print(x+'!')
x = input()
print(x)
name = input("Enter your name: ")
print("Hello, "+name)
age = int(input())
print(age)
age = 42
print("His age is " + str(age))
x = "2"
y = "4"
z = int(x) + int(y)
print(z)
name = input()
age = input()
print(name + " is " + age)
x = 2
print(x)
x += 3
print(x)
x = 4
x *= 3
print(x)
x = "spam "
print(x)
x += "eggs"
print(x)
spam = "7"
spam = spam + "0"
eggs = int(spam) + 3
print(float(eggs))
x = input()
y = input()
z = int(x) + int(y)
print(z)
my_boolean = True
print(my_boolean)
print(2 == 3)
print("hello" == "hello")
print(1 != 1)
print("eleven" != "seven")
print(2 != 10)
print(7 > 5)
print(10 < 10)
print(11.0 > 11)
print(7 <= 8)
print(9 >= 9.0)
print("Annie" > "Andy")
if 10 > 5:
    print("10 greater than 5")
print("Program ended")

num = 12
if num > 5:
    print("Bigger than 5")
    if num <= 47:
        print("Between 5 and 47")
x = 4
if x == 5:
    print("Yes")
else:
    print("No")
num = 3
if num == 1:
    print("one")
else:
    if num == 2:
        print("two")
    else:
        if num == 3:
            print("three")
        else:
            print("something else")
num = 3
if num == 1:
    print("one")
elif num == 2:
    print("two")
elif num == 3:
    print("three")
else:
    print("something else")
print(1 == 1 and 2 == 2)
print(1 == 1 and 2 == 3)
print(1 != 1 and 2 == 2)
print(2 < 1 and 3 > 6)
print(1 == 1 or 2 == 2)
print(1 == 1 or 2 == 3)
print(1 != 1 or 2 == 2)
print(2 < 2 or 3 > 6)
print(not 1 == 7)
print(not 1 > 7)
print(False == False or True)
print(False == (False or True))
print((False == False) or True)
grade = 88
if (grade >= 70 and grade <= 100):
    print("passed")
grade = 88
if (70 <= grade <= 100):
    print("passed")
words = ["hello", "word", "!"]
print(words[0])
print(words[1])
print(words[2])
empty_list = []
print(empty_list)
number = 3
things = ["string", 0, [1, 2, number], 4.56]
print(things[1])
print(things[2])
print(things[2][2])
m = [
    [1, 2, 3],
    [4, 5, 6]
]
print(m[1][2])
str = "hello world"
print(str[6])
nums = [7, 7, 7, 7, 7]
nums[2] = 5
print(nums)
nums = [1, 2, 3]
print(nums + [4, 5, 6])
print(nums * 3)
words = ["spam", "egg", "spam", "sausage"]
print("spam" in words)
print("egg" in words)
print("tomato" in words)
nums = [1, 2, 3]
print(not 4 in nums)
print(4 not in nums)
print(not 3 in nums)
print(3 not in nums)
nums = [1, 2, 3]
nums.append(4)
print(nums)
nums = [1, 3, 5, 2, 4]
print(len(nums))
words = ['Python', 'fun']
index = 1
words.insert(index, 'is')
print(words)
letters = ['p', 'q', 'r', 's', 'p', 'u']
print(letters.index('r'))
print(letters.index('p'))
print(letters.index('z'))
i = 1
while i <= 5:
    print(i)
    i = i + 1

print('Finished')
