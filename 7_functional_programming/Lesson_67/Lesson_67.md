```rootsql
67.1 Генераторы
# Генераторы представляют собой итерируемый тип, такой как списки или кортежи. 
В отличие от списков им нельзя присваивать произвольные индексы, но они поддерживают циклы for. 
Они создаются с использованием функций и инструкции yield.
# Инструкция yield определяет генератор, заменяет значение, возвращаемое функцией, и возвращает результат, 
не меняя первоначальные переменные.
```
```rootsql
67.2 Генераторы
# Так как генераторы возвращают по одному элементу за раз, они, в отличие от списков, не имеют ограничений по памяти. 
На самом деле, они могут выполняться бесконечно!
# Подсуммируем: генераторы позволяют объявить функцию, которая подобна итератору, т.е. может быть использована в цикле.
```
```rootsql
67.3 Генераторы
# Конечные генераторы могут быть преобразованы в списки, для этого их нужно передать как аргументы функции list
# Использование генераторов позволяет повысить производительность: 
«ленивая» генерация значений (генерация по требованию) означает сниженное потребление памяти. 
Кроме того, не нужно ждать, пока все элементы будут сгенерированы, мы можем начать их использовать гораздо раньше.
```
