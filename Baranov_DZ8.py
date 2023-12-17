import json
import csv

 #Zadanie 1
# code = b'r\xc3\xa9sum\xc3\xa9'
# code_decode = code.decode()
# print(f"{code_decode}\n")
# code_latin = code_decode.encode("Latin1")
# print(f"{code_latin}\n")
# code_latin1 = code_latin.decode('Latin1')
# print(f"{code_latin1}\n")
#
# #Zadanie 2
# st1 = input()
# st2 = input()
# st3 = input()
# st4 = input()
# f = open('newdoc_br.txt', 'w')
# f.write(f'{st1}\n{st2}\n')
# f.close()
# f = open('newdoc_br.txt', 'a')
# f.write(f'{st3}\n{st4}\n')
# f.close()

#Zadanie 3

# sl = {
#     111111: ("Sasha", 23),
#     222222: ("Denis", 22),
#     333333: ("Marina", 25),
#     444444: ("Evgen", 26),
#     555555: ("Lyda", 27),
# }
# with open("sl.json", "w") as file:
#     json.dump(sl, file)

#Zadanie 4
with open("../sl.json", "r") as file:
    new_sl = json.load(file)
    number_sl = ["id", "name", "age", "number"]
with open("../new_sl1.csv", "w") as csv_file:
    write = csv.DictWriter(csv_file, fieldnames = number_sl)
    write.writeheader()
    for key, values in new_sl.items():
        write.writerow({"id": key, "name": values[0], "age": values[1], "number": ""})