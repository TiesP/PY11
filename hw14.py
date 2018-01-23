# необходимо получить list из кубов всех чисел, делящихся и на 3,
# и на 4 без остатка, взятых из массива чисел mass.
# Использовать List Comprehensions.
mass = [1, 2, 3, 4, 5, 12, 13, 18, 20, 24]
result = [n**3 for n in mass if not n % 12]
print(result)
