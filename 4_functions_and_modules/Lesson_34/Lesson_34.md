```rootsql
34.1 Аргументы
# Все рассмотренные до сих пор определения функций были функциями без аргументов, то есть с пустыми круглыми скобками. 
Но обычно функции принимают какие-то аргументы.
В примере внизу определена функция, у которой один аргумент:
def print_with_exclamation(word):
   print(word + "!")
print_with_exclamation("spam")
print_with_exclamation("eggs")
print_with_exclamation("python")
# Как видите, аргумент определяется в круглых скобках.
```
```rootsql
34.2 Параметры
# Если нужно определить функцию с более чем одним аргументом, они указываются через запятую.
```
```rootsql
34.3 Аргументы
# Аргументы функции могут быть использованы в качестве переменных внутри определения функции. 
Но на них нельзя ссылаться извне определения функции. Это также относится и к другим переменным, созданным в теле функции.
def function(variable):
    variable += 1
    print(variable)
    function(7)
print(variable)
Этот код выведет ошибку, потому что переменная variable определена внутри функции и на нее можно ссылаться только там.
# Практически параметры - это переменные в теле функции, а аргументы - значения, присваиваемые параметрам при вызове функции.
```