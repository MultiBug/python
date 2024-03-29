```rootsql
47.1 Открытие файлов
# С помощью Python можно читать и редактировать содержимое файлов.
Легче всего работать с текстовыми файлами. Перед редактированием файл нужно открыть, 
что можно сделать с помощью функции open.
# Аргумент функции open - путь к файлу. Если файл находится в текущей рабочей директории программы, 
можно задать только его имя.
```
```rootsql
47.2 Открытие файлов
# Вы можете указать режим, в котором нужно открыть файл, добавив второй аргумент в заголовок функции open.
Если указать "r", файл будет открыт в режиме чтения; этот режим используется по умолчанию; 
"w" - файл будет открыт в режиме записи;
"а" - файл будет открыт в режиме добавления: новый контент будет добавляться в конец файла;
"b" - файл будет открыт в двоичном режиме, который используется для нетекстовых файлов 
(таких как изображения и звуковые файлы).
    write mode:
open("filename.txt", "w")
    read mode:
open("filename.txt", "r")
open("filename.txt")
    binary write mode:
open("filename.txt", "wb")
# Вы можете использовать знак + в каждом из режимов выше, чтобы предоставить им дополнительный доступ к файлам. 
Например, r+ открывает файл для чтения и записи.
```
```rootsql
47.3 Открытие файлов
# После того, как вы открыли файл и поработали с ним, его нужно закрыть.
Это делается с помощью метода close, указанного в качестве объекта файла.
# Мы научимся читать/записывать контент файлов немного позже.
```