#Ввід множин з клавіатури
def inputing():
    universal=noSpaces(input("Множина U:\n").split(" "))
    set1=noSpaces(input("Множина A:\n").split(" "))
    belongsToUniversal(set1, universal)
    set2=noSpaces(input("Множина B:\n").split(" "))
    belongsToUniversal(set2, universal)
    print(universal, " | ", set1, set2)
    return set1, set2, universal

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

#Перевірка множин на належність універсальній
def belongsToUniversal(set: list, universal: list):
    for i in set:
        if not universal.count(i):
            raise Exception(f"Множина {set} не є частиною універсальної.")

#Перевірка чи є підмножиною чи рівні
def isSubsetOrEqual(arr1: list, arr2:list):
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

#Переведення з бітового рядка у множину
def bitToNormal (arrbits: list, universal: list):
    arr =[]
    for i in range(len(arrbits)):
        if arrbits[i]:
            arr.append(universal[i])
    return arr
            
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
def addition(arr1: list, universal: list):
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

def bitline(arr1: list, arr2: list, universal: list):
    arr1bits = []
    arr2bits = []
    for i in universal:
        if arr1.count(i) == 1:
            arr1bits.append(1)
        else:
            arr1bits.append(0)
    for j in universal:
        if arr2.count(j) == 1:
            arr2bits.append(1)
        else:
            arr2bits.append(0)
    print(f"Бітовий рядок для першої множини: {arr1bits}")
    print(f"Бітовий рядок для другої множини: {arr2bits}")
    return arr1bits, arr2bits


def bitoperations(arr1bits: list, arr2bits: list, universal: list):
    #Об'єднання
    connectingbits = []
    for i in range(len(arr1bits)):
        if arr1bits[i] or arr2bits[i]:
            connectingbits.append(1)
        else:
            connectingbits.append(0)
    connecting = bitToNormal(connectingbits, universal)
    print(f"Бітова операція об'єднання над множинами дала результат: {connectingbits}\nАбо у числовому вигляді: {connecting}")

    #Перетин
    crossbits = []
    for i in range(len(arr1bits)):
        if arr1bits[i] and arr2bits[i]:
            crossbits.append(1)
        else:
            crossbits.append(0)
    cross = bitToNormal(crossbits, universal)
    print(f"Бітова операція перетину над множинами дала результат: {crossbits}\nАбо у числовому вигляді: {cross}")

    #Різниця 
    diffbits = []
    for i in range(len(arr1bits)):
        if arr1bits[i] and not arr2bits[i]:
            diffbits.append(1)
        else:
            diffbits.append(0)
    diff = bitToNormal(diffbits, universal)
    print(f"Бітова операція різниці над множинами дала результат: {diffbits}\nАбо у числовому вигляді: {diff}")

    #Симетрична різниця
    symdiffbits = []
    for i in range(len(arr1bits)):
        if (arr1bits[i] and not arr2bits[i]) or (not arr1bits[i] and arr2bits[i]):
            symdiffbits.append(1)
        else:
            symdiffbits.append(0)
    symdiff = bitToNormal(symdiffbits, universal)
    print(f"Бітова операція симетричної різниці над множинами дала результат: {symdiffbits}\nАбо у числовому вигляді: {symdiff}")
    




#Варіант 25
print("Лабораторна робота з СРМ1 №3\nВаріант 25\nТунік Олександр | ІА-34\n")    

print("Треба ввести 2 множини. Вводити числа через один пропуск.")
set1, set2, universal = inputing()
connecting(set1, set2)
crossing(set1, set2)
difference(set1, set2)
addition(set1, universal)
symetrDiff(set1, set2)
dekartMultiply(set1, set2)
bitset1, bitset2 = bitline(set1, set2, universal)
bitoperations(bitset1, bitset2, universal)
isSubsetOrEqual(set1, set2)