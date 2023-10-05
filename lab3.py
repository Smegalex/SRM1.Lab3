import numpy as np

#Варіант 25
print("Лабораторна робота з СРМ1 №3\nВаріант 25\nТунік Олександр | ІА-34\n")

#Видалення зайвих пропусків  з множини
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

#Ввід множин з клавіатури
def inputing(amount: int):
    set1=noSpaces(input("Множина 1:\n").split(" "))
    set2 = []
    if amount == 2:
        set2=noSpaces(input("Множина 2:\n").split(" "))
    print(set1, set2)
    return set1, set2

#Перевірка чи є підмножиною чи рівні
def isSubset(arr1: list, arr2:list):
    counter = 0
    if len(arr1)<len(arr2):
        for i in arr1:
            if arr2.count(i) > 0:
                counter += 1
            if counter == len(arr1):
                print(f"Множина {arr1} є підмножиною множини {arr2}.")
    elif len(arr2)<len(arr1):
        for j in arr2:
            if arr1.count(j) > 0:
                counter += 1
            if counter == len(arr2):
                print(f"Множина {arr2} є підмножиною множини {arr1}.")
    else:
        areEqual(arr1, arr2)

#Перевірка чи рівні
def areEqual(arr1: list, arr2: list):
    counter = 0
    if len(arr1)==len(arr2):
        for i in arr1:
            if arr1.count(i) == arr2.count(i):
                counter += 1
        if counter == len(arr1):
            print("Множини рівні.")
            return True
    else:
        return False
            
#Об'єднання
def connecting(arr1: list, arr2: list):
    final = []
    for i in arr1:
        if final.count(i) < 1:
            final.append(i)
    for j in arr2:
        if final.count(j) < 1:
            final.append(j)
    print(f"Об'єднання цих множин:\n{final}")
    return final

#Перетин
def crossing(arr1: list, arr2: list):
    final = []
    for i in arr1:
        if arr2.count(i) > 0 and final.count(i) == 0:
            final.append(i)
    for j in arr2:
        if arr1.count(j) > 0 and final.count(j) == 0:
            final.append(j)  
    print(f"Перетин цих множин:\n{final}")
    return final  

#Різниця
def difference(arr1: list, arr2: list):
    final = []
    for i in arr1:
        if arr2.count(i) == 0 and final.count(i) == 0:
            final.append(i)
    print(f"Різниця цих множин:\n{final}")
    return final 

#Доповнення
def addition(arr1: list):
    print("Введіть універсальну множину U:")
    universal, nothing = inputing(1)
    final = []
    for i in universal:
        if arr1.count(i) == 0 and final.count(i) == 0:
            final.append(i)
    print(f"Доповнення множини 1:\n{final}")
    return final 

#Симетрична різниця
def symetrDiff(arr1: list, arr2: list):
    final = []
    for i in arr1:
        if arr2.count(i) == 0 and final.count(i) == 0:
            final.append(i)
    for j in arr2:
        if arr1.count(j) == 0 and final.count(j) == 0:
            final.append(j)
    print(f"Симетрична різниця цих множин:\n{final}")
    return final

#Декартовий добуток
def dekartMultiply(arr1: list, arr2: list):
    final = []
    for i in arr1:
        for j in arr2:
            if final.count((i, j)) == 0:
                final.append((i, j))
    print(f"Декартовий добуток цих множин:\n{final}")
    return final     

    

print("Треба ввести 2 множини. Вводити числа через один пропуск.")
set1, set2 = inputing(2)
connecting(set1, set2)
crossing(set1, set2)
difference(set1, set2)
#addition(set1)
symetrDiff(set1, set2)
dekartMultiply(set1, set2)
isSubset(set1, set2)