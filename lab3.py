import numpy as np

#Варіант 25
print("Лабораторна робота з СРМ1 №3\nВаріант 25\nТунік Олександр | ІА-34\n")

def noSpaces(set: list):
    i = 0
    while True:
        if i >= len(set):
            break
        if set[i]=="":
            set.pop(i)
            continue
        i+= 1

    return set


set1 = [];
set2 = [];

def inputing():
    print("Треба ввести 2 множини. Вводити числа через один пропуск.")
    set1=noSpaces(input("Множина 1:\n").split(" "))
    set2=noSpaces(input("Множина 2:\n").split(" "))
    
    print(set1, set2)

inputing()