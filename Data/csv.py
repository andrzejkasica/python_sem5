import csv
import os

rank = []
name = []
surname = []

with open("C:\\Users\\Admin\\source\\repos\\hello_world\\hello_world\\Data\\data.csv", 'r') as Dat:
    lines = Dat.read().splitlines()
    print(lines)
    for i in lines:
        rank.append(i.split(" , ")[0])
        name.append(i.split(" , ")[1])
        surname.append(i.split(" , ")[2])
     
    Dat.close()

rank[0] = "Numer"
name[0] = "Imie"
surname[0] = "Nazwisko"

while 1:
    print("Wybierz:\n1. Dodaj wiersz\n2. Usun wiersz\n3. Wyswietl zawartosc\n4. Zamknij")
    s = input(": ")
    if s =='1':
        rank.append(str(len(rank)))
        name.append(str(input("Podaj imie\n")))
        surname.append(str(input("Podaj nazwisko\n")))
    elif s=='2':
        i = int(input("Usun wiersz: "))
        del name[i]
        del surname[i]
    elif s=='3':
        with open("C:\\Users\\Admin\\source\\repos\\hello_world\\hello_world\\Data\\data.csv", 'r') as Dat:
            lines = Dat.read().splitlines()
            print(lines)
    else: 
        break

save =[]

with open("C:\\Users\\Admin\\source\\repos\\hello_world\\hello_world\\Data\\data.csv", 'r') as date_save:
    for i in range (0,len(rank)):
        save.append(rank[i] + " , " + name[i]+ " , "+ surname[i]+ "\n")
    date_save.writelines(save)
date_save.close()