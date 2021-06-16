########################
# Решение задачи 54.3 'Управление складом':
store = {"Orange": 2, "Watermelon": 0, "Apple": 8, "Banana": 42}
print(store["Apple"])
########################
########################
# Решение задачи 55.2 'Управление библиотекой':
books = {
    "Life of Pi": "Adventure Fiction",
    "The Three Musketeers": "Historical Adventure",
    "Watchmen": "Comics",
    "Bird Box": "Horror",
    "Harry Potter":"Fantasy Fiction",
    "Good Omens": "Comedy"
}
book = input()
if book in books:
    print(books[book])
else:
    print("Not found")
########################
########################
# Решение задачи 55.3 'Где книга?':
books = {
    "Life of Pi": "Adventure Fiction",
    "The Three Musketeers": "Historical Adventure",
    "Watchmen": "Comics",
    "Bird Box": "Horror",
    "Harry Potter":"Fantasy Fiction",
    "Good Omens": "Comedy"
}
book = input()
print(books.get(book, "Book not found"))
########################
########################
# Решение задачи 56.2 'Кортежи':
import math
p1 = (23, -88)
p2 = (6, 42)
p = math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)
print(p)
########################
########################
# Решение задачи 57.4 'Элементы списка':

########################
