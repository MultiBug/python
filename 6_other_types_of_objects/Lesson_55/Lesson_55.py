####################################
# 54.1 Словари
squares = {1: 1, 2: 4, 3: "error", 4: 16,}
squares[8] = 64
squares[3] = 9
print(squares)
####################################
####################################
# 54.2 Словари
nums = {
    1: "one",
    2: "two",
    3: "three",
}
print(1 in nums)
print("three" in nums)
print(4 not in nums)
####################################
####################################
# 54.3 Словари
pairs = {1: "apple",
    "orange": [2, 3, 4],
    True: False,
    None: "True",
}
print(pairs.get("orange"))
print(pairs.get(7))
print(pairs.get(12345, "not in dictionary"))
####################################
