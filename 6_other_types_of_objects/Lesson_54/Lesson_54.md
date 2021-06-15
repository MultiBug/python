```rootsql
54.1 Словари
# Словари являются структурами данных, которые используются для хранения произвольных ключей и заданных им значений. 
Списки, к слову, могут рассматриваться как словари с ключами в виде целых чисел в пределах заданного диапазона.
Словари могут быть проиндексированы таким же образом, как списки, используя квадратные скобки с ключами внутри них.
# Каждый элемент в словаре выражен в форме key:value.
```
```rootsql
54.2 Словари
# Попытка сослаться на ключ, которого нет в словаре, возвращает ошибку KeyError.
# Пустой словарь обозначается {}.
```
```rootsql
54.3 Словари
# Только объекты immutable могут быть использованы в качестве ключей словарей. Объекты immutable не могут быть изменены. 
До сих пор единственными изменяемыми объектами в этом курсе, были списки и словари. 
Попытка использовать изменяемый объект в качестве ключа словаря вызывает TypeError.
```