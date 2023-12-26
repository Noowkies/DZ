#Zadanie 1
class Publication:
    publisher = 'Penguin Publishing'

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def display(self):
        return f'Title: {self.title}\nAuthor: {self.author}\nYear: {self.year}'

    @classmethod
    def get_publisher(cls):
        return f'Publisher: {cls.publisher}'


class Book(Publication):
    def __init__(self, title, author, year, isbn='0-000-00000-0'):
        super().__init__(title, author, year)
        self.isbn = isbn

    def display(self):
        return super().display() + f'\nISBN: {self.isbn}'


class Magazine(Publication):
    def __init__(self, title, author, year, issue_number):
        super().__init__(title, author, year)
        self.issue_number = issue_number

    def display(self):
        return super().display() + f'\nISBN: {self.issue_number}'


book1 = Book('One Trick Pony', 'D. Nguyen', 2014, '1-123-12345-1')
print(book1.display())
print(book1.get_publisher())

#Zadanie 2
#
# class BankAccount:
#     def __init__(self, balance, interest_rate):
#         self._balance = balance
#         self._interest_rate = interest_rate
#         self._transactions = []
#
#     def deposit(self, amount):
#         if amount > 0:
#             self._balance += amount
#             self._transactions.append(f'Add {amount} to your account.')
#             print(f'Total: {self._balance}')
#         else:
#             print('Wrong amount!')
#
#     def withdraw(self, amount):
#         if amount > 0:
#             self._balance -= amount
#             self._transactions.append(f'Subtract {amount} from your account.')
#             print(f'Total: {self._balance}')
#         else:
#             print('Wrong amount!')
#
#     def add_interest(self):
#         interest = self._balance * self._interest_rate / 100
#         self._balance += interest
#         self._transactions.append(f'Add {interest} to your account.')
#         print(f'Total: {self._balance}')
#
#     def history(self):
#         for transaction in self._transactions:
#             print(transaction)
#
#
# account = BankAccount(100, 5)
# account.deposit(10)
# account.withdraw(25)
# account.add_interest()
# account.history()