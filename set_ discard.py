'''
discard(elem) — видаляє елемент із множини і не викликає виняток, якщо його немає

'''

numbers = {1, 2, 3}
numbers.discard(2)
print(numbers)  # {1, 3}
