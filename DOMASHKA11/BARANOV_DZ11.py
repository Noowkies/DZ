#Zadanie 1
class Publication:
    publisher = 'AST'

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def display(self):
        return f'Title: {self.title}\n Author: {self.author}\n Year: {self.year}'

    @classmethod
    def get_publisher(cls):
        return f'Publisher: {cls.publisher}'

class Book(Publication):
    def __init__(self, title, author, year, isbn='1-101-10001-1'):
        super().__init__(title, author, year)
        self.isbn = isbn

    def display(self):
        return super().display() + f'\n ISBN: {self.isbn}'


class Magazine(Publication):
    def __init__(self, title, author, year, issue_number):
        super().__init__(title, author, year)
        self.issue_number = issue_number

    def display(self):
        return super().display() + f'\n ISBN: {self.issue_number}'


books = Book('Harry Potter', 'JK Roaling', 2008, '2-202-20002-2')
print(books.display())
print(books.get_publisher())

#Zadanie 2

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
#         interest = self._balance * self._interest_rate / 50
#         self._balance += interest
#         self._transactions.append(f'Add {interest} to your account.')
#         print(f'Total: {self._balance}')
#
#     def history(self):
#         for transaction in self._transactions:
#             print(transaction)
#
#
# account = BankAccount(1000, 3)
# account.deposit(50)
# account.withdraw(75)
# account.add_interest()
# account.history()