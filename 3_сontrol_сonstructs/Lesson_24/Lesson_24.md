```rootsql
24.1 Списки
# Списки (list) используются для хранения элементов.
Список создается с помощью квадратных скобок и запятых, разделяющих элементы.
# Элемент списка может быть вызван с помощью его индекса, указанного в квадратных скобках.
# Обратите внимание, первый элемент списка имеет индекс 0, а не 1.
```
```rootsql
24.2 Списки
# Иногда нужно создать пустой список, чтобы позднее поместить туда элементы. 
Например, если вы создаете программу для управления очередью, то в начале очередь будет пустой, 
а потом в ней появятся люди - элементы списка.
Чтобы создать пустой список, используйте пустые квадратные скобки.
# Иногда в списке вы можете увидеть запятую после последнего элемента. Это не обязательно, но вполне допустимо
```
```rootsql
24.3 Списки
# Как правило, список содержит элементы одного типа, но также может содержать элементы различных типов. 
Список может находиться внутри другого списка.
# Вложеннные листы могут представлять двумерную матрицу:
m = [
    [1, 2, 3],
    [4, 5, 6]
    ]
print(m[1][2])
# Структуры, подобные матрицам, могут быть использованы, когда нужно сохранить данные в формате таблицы (строки-колонки). 
Например, при создании программы для распределения билетов, номера сидений могут быть помещены в матрицу, 
в соответствующую строку и колонку.
# Код свыше выводит 3-й элемент 2-й строки.
```
```rootsql
24.4 Списки
# Некоторые типы данных, такие как строки, могут быть проиндексированы, как списки.
При индексации строк, каждый символ в строке будет проиндексирован, как отдельный элемент списка.
# Пробел (" ") тоже символ и имеет индекс.
# Попытка вызвать несуществующий элемент списка вызывает ошибку IndexError.
```