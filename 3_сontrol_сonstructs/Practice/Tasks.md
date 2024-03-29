```rootsql
Задача 21.1 'Вышибала в ночном клубе':

Напишите программу для контроля за входом в клуб.
В клуб допускаются люди, которым 18 лет и больше.
Ваша программа берет возраст и имя человека, который пытается войти, и выводит "Welcome" и имя этого человека, 
если им разрешено входить в клуб, и "Sorry", если он младше дозволенного возраста.
Пример ввода
24
James
Пример вывода 
Welcome James

Подсказка:

Не забудьте поставить пробел между "Welcome" и именем человека.
```
```rootsql
Задача 21.2 'Пифагор или нет?':

Теорема Пифагора гласит: В прямоугольном треугольнике квадрат гипотенузы равен сумме квадратов катетов.
Напишите программу, которая берет длину сторон треугольника в качестве ввода и выводит утверждение о том, 
является ли наш треугольник прямоугольным. Если треугольник прямоугольный, программа должна вывести "Right-angled", 
а если нет — "Not right-angled".
Пример ввода
3
4
7
Пример вывода
Not right-angled

Подсказка:

Примите 3-й ввод (переменная side3 в коде из примера) за самую длинную сторону, которая будет являться гипотенузой, 
если треугольник является прямоугольным.
```
```rootsql
Задача 21.3.1 'Робот, который любит порядок':

Напишите программу, которая потребуется для того, чтобы робот смог распределять предметы по цвету.
Предмет каждого цвета отправляется в соответствующую коробку с номером.
Для удобства наша программа будет определять 3 цвета:
red отправляется в коробку #1
green отправляется в коробку #2
black отправляется в коробку #3
Ваша программа должна использовать цвет в качестве ввода и выводить соответствующий номер коробки.
Пример ввода
green
Пример вывода
2

Подсказка:

Помните, что вы можете использовать выражение if/elif/else для проверки разных состояний.
```
```rootsql
Задача 21.3.2 'Учитывая четность':

Напишите программу, которая берет число в качестве ввода и
- возвращает удвоенное число, если оно четное
- возвращает утроенное число, если оно нечетное
- возвращает 0, если число равно 0
Пример ввода:
1
Пример вывода:
3

Подсказка:

Целое число является четным, если делится на два, в противном случаем оно является нечетным.
```
```rootsql
Задача 22.1 'Магазин закрыт!':

Вам необходимо создать программу, которая выводит состояние магазина Open или Closed в зависимости от времени и дня недели.
Магазин открыт ежедневно с 10 до 21, кроме субботы и воскресенья.
Вам необходимо добавить час и день недели в качестве ввода.
День недели представлен в виде целого числа (1 для понедельника, 2 для вторника и т. д.)
Пример ввода:
15
4
Пример вывода:
Открыть

Подсказка:

Объяснение: Магазин открыт в 15:00 по четвергам (4 представляет четверг).
```
```rootsql
Задача 22.3 'Возрастные группы':

Принимая возраст человека в качестве ввода, выведите их возрастную группу.
Ниже представлены возрастные группы:
Child: 0 – 11
Teen: 12 – 17
Adult: 18 – 64
Senior: 65+
Пример ввода
42
Пример вывода
Adult

Подсказка:

Помните, что вы можете использовать логический оператор and для сочетания условий. Например, x>0 and x<20.
```
```rootsql
Задача 23.2 'Скидка на обучение':

Университет предоставляет студентам скидки на оплату обучения в зависимости от их успеваемости:
90-100 => 50%
80-89   => 30%
70-79   => 10%
0-69     => 0%
Напишите программу, которая берет оценки за первый и второй семестр, 
а затем рассчитывает среднее значение и выводит результат в зависимости от оценки.
Пример ввода
67
83
Пример вывода
10
Объяснение
Среднее между 67 и 83 — 75, что в пределах диапазона 70-79, а значит, скидка составляет 10%.

Подсказка:

Среднее — это сумма чисел, поделенная на количество этих чисел. Например, среднее между 5,6,7 составляет (5+6+7)/3 = 6.
```
```rootsql
Задача 24.2 'Автомат с фруктами':

Представьте торговый автомат с фруктами. У каждого фрукта свой номер, начиная с 0.
Напишите программу для торгового автомата, которая возьмет число n в качестве ввода от покупателя и выдаст фрукт, 
который соответствует данному числу.
If n< 0 or  n>7 (the index of last fruit ), program outputs "Wrong number".
Пример ввода:
2
Пример вывода:
banana

Подсказка:

Помните, что первый элемент в списке имеет индекс 0.
```
```rootsql
Задача 24.4 'Каждый третий знак':

Помните, что строки можно индексировать как списки.
Напишите программу, которая берет строку ввода и выводит 3-ий знак этой строки.
Пример ввода
Hello
Пример вывода
l

Подсказка:

Помните, что первый элемент имеет индекс 0.
```
```rootsql
Задача 25.2 'Операции со спискoм':

Вам дан список предметов. 
Напишите программу, которая берет число num в качестве ввода, 
переназначает элемент с этим индексом в списке значению "x" и выводит обновленный список.
Например, в случае списка [1, 2, 3, 4, 5] и значения 3, вывод должен быть:
[1, 2, 3, "x", 5]

Подсказка:

Четвертое значение было переназначено, поскольку индексация списка начинается с 0.
```
```rootsql
Задача 25.3.1 'Создаем поисковый механизм':

Вы создаете поисковую систему, и вам необходимо найти букву 'a' в строке ввода.
Выведите "Match" если в строке есть 'a', и "No match", если нет.
Пример ввода
great
Пример вывода 
Match

Подсказка:

Чтобы проверить, находится ли элемент в списке, можно воспользоваться оператором in.
```
```rootsql
Задача 25.3.2 'Бинго!':

Имеется список чисел. Выведите "bingo" если он содержит введенное число.

Подсказка:

Не выводите ничего, если номер не найден.
```
```rootsql
Задача 26.1 'Управление очередью':

Вы работаете над программой управления очередью.
Очередь представлена списком. 
Напишите программу, которая получит ввод, добавит его в конец очереди и выведет полученный список.

Подсказка:

Можно использовать метод append() для добавления нового элемента в список.
```
```rootsql
Задача 26.2 'Средний элемент':

Имеется список. Вычислите индекс элемента, который находится по середине списка.

Подсказка:

Вы можете использовать функцию len(), чтобы получить число элементов в списке и затем поделить его на 2 с остатком, 
используя двойную косую черту (//).
```
```rootsql
Задача 26.4 'Минимум и Максимум':

Вам дан список:
numbers = [14, 5, 6, 8, 17, 28]
Напишите программу, которая рассчитает и выведет сумму максимального и минимального значений списка.

Подсказка:

Можно воспользоваться функциями max(list) and min(list) для получения соответствующих значений.
```
```rootsql
Задача 27.1 'Четные числа':

x = 0
while x <= 10:
    print(x)
    x += 1
Перед вами программа, которая выводит все числа от 0 до 10.
Измените код таким образом, чтобы она выводила только четные числа.

Подсказка:

Каждое целое число, которое можно разделить на 2, является четным.
```
```rootsql
Задача 27.2 'Сумма цифр':

Имеющаяся программа рассчитывает и выводит количество цифр в виде определенного числа при помощи цикла while.
n = int(input())
length = 0
while n > 0:
    n //= 10
    length += 1   
print(length)
В ходе каждой итерации цикл использует деление с остатком, чтобы разделить число на 10, то есть перенося запятую влево. 
Процесс продолжается до тех пор, пока не останется ни одной цифры (n>0).
Вам необходимо изменить код, чтобы рассчитать и вывести сумму всех цифр введенного числа.
Пример ввода
643
Пример вывода
13
Объяснение
Сумма чисел 643 составляет 6+4+3 = 13.

Подсказка:

Вы можете получить каждую цифру числа путем деления на 10 с остатком modulo (%) в каждой итерации
```
```rootsql
Задача 27.3 'Бесконечные циклы':

Имеющийся код использует бесконечный цикл для непрерывного получения пользовательского ввода. 
В ходе каждой итерации пользовательский ввод добавляется в список элементов.
Измените код, чтобы прекратить цикл, когда пользователь вводит 0.
Выведите полученный список после окончания цикла while.
Пример ввода
1
2
3
0
Пример вывода
[1, 2, 3]

Подсказка:

Не добавляйте 0 в список.
```
```rootsql
Задача 27.4 'Сегодня акция!':

Сегодня в магазине акция! Если цена товара является четным числом, вы получаете товар бесплатно!
Используйте список для сохранения цен на все товары в корзине.
Имеющийся код использует цикл while для итерации списка, вычисляет цену всех товаров в списке и выводит результат.
Измените код, чтобы пропустить нечетные цены, вычислить сумму только четных цен и вывести результат.

Подсказка:

Используйте выражение continue, чтобы пропустить итерации с четными числами.
```
```rootsql
Задача 28.3 'Итерация':

Циклы for позволяют с легкостью выполнять итерации по списку.
Имея список чисел, выведите их сумму.
Пример ввода
1 3 7 5
Пример вывода 
16

Подсказка:

Выведите сумму после завершения цикла.
```
```rootsql
Задача 29.4 'Выбор даты':

Вы разрабатываете подборщик дат для сайта, и вам необходимо вывести все годы за определенный период. 
Напишите программу, берущую два целых числа в качестве ввода и выводящую диапазон чисел между двумя вводами в виде списка.
Последовательность вывода должна начинаться с первого введенного числа и заканчиваться вторым введенным числом, не включая его.
Пример ввода
2005
2011
Пример вывода 
[2005, 2006, 2007, 2008, 2009, 2010]

Подсказка:

Вы можете преобразовать объект range в список и вывести его.
```
```rootsql
Задача 29.4 31 'FizzBuzz':

FizzBuzz — это популярная задача, которая часто дается в ходе собеседования.
n = int(input())
for x in range(1, n):
    if x % 3 == 0 and x % 5 == 0:
        print("SoloLearn")
    elif x % 3 == 0:
        print("Solo")
    elif x % 5 == 0:
        print("Learn")
    else:
        print(x)
Предложенный код разрешает проблему FizzBuzz и использует слова "Solo" и "Learn" вместо "Fizz" и "Buzz". 
Он берет ввод n и выводит числа от 1 до n.
Для каждого числа, кратного 3, печатает "Solo" вместо числа. 
Для каждого числа, кратного 5, печатает "Learn" вместо числа. 
Для чисел, кратных 3 и 5, выводит "SoloLearn". 
Вам необходимо написать код, чтобы пропускать четные числа, 
чтобы данная логика применялась только к нечетным числам диапазона.

Подсказка:

Помните, что выражение continue можно использовать для пропуска итерации цикла.
```