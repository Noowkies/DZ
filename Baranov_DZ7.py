#Zadanie 1
from datetime import datetime
def working_hours_only(func):
    def wrapper():
        a = datetime.strptime('9:00', '%H:%M').time()
        b = datetime.strptime('18:00','%H:%M').time()
        time = datetime.now().time()
        if a <= time <= b:
            func()
        else:
            print("Не работаем")
    return wrapper

@working_hours_only
def work():
    print("Работаем")
work()

#Zadanie 2
def decorator(type_check):
    def wrapper(func):
        def a(arg):
            if type(arg) is (type_check):
                return func(arg)
            return "Bad type"
        return a
    return wrapper


@decorator(int)
def times2(num):
    return num*2

print(times2(2))
print(times2(True))

@decorator(str)
def first_letter(word):
    return word[0]

print(first_letter("Hello world"))
print(first_letter(1.5))