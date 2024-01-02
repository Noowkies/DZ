#Zadanie 1
# class CardDeck:
#     def __init__(self):
#         self.length = 52
#         self.index = 0
#         self.__SUITS = ['Пик', 'Бубей', 'Червей', 'Крестей']
#         self.__RANKS = [*range(2, 11), 'J', 'Q', 'K', 'ace']
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index < self.length:
#             s = self.__SUITS[self.index // len(self.__RANKS)]
#             r = self.__RANKS[self.index % len(self.__RANKS)]
#             self.index += 1
#             return f'{r} {s}'
#         else:
#             raise StopIteration
#
#
#
# deck = CardDeck()
# while True:
#     print(next(deck))

#Zadanie 2

def fib(n):
    a, b = 0, 1
    for __ in range(n):
        yield a
        a, b = b, a + b


print(list(fib(int(input("Введите число: ")))))