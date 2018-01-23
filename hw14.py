# необходимо получить list из кубов всех чисел, делящихся и на 3,
# и на 4 без остатка, взятых из массива чисел mass.
# Использовать List Comprehensions.
mass = [1, 3, 5, 12, 13, 24]
result = [n for n in mass if not n % 12]
print(result)
